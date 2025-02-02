import argparse
import json
import logging
import time
import urllib.robotparser
from collections import deque
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.exceptions import RequestException
from urllib3.util.retry import Retry

class WikipediaCrawler:
    def __init__(self, config):
        self.base_url = "https://en.wikipedia.org"
        self.start_url = config['start_url']
        self.max_pages = config['max_pages']
        self.request_delay = config['request_delay']
        self.output_file = config['output_file']
        self.user_agent = config['user_agent']
        
        self.visited_urls = set()
        self.session = self._create_session()
        self.robots_parser = self._init_robots_txt()
        
        self.logger = self._setup_logging()
        self.data_buffer = []

    def _create_session(self):
        session = requests.Session()
        retry = Retry(
            total=5,
            backoff_factor=0.1,
            status_forcelist=[500, 502, 503, 504]
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session

    def _init_robots_txt(self):
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(urljoin(self.base_url, "/robots.txt"))
        try:
            rp.read()
        except Exception as e:
            self.logger.error(f"Error reading robots.txt: {e}")
        return rp

    def _setup_logging(self):
        logger = logging.getLogger('wiki_crawler')
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def _is_allowed(self, url):
        return self.robots_parser.can_fetch(self.user_agent, url)

    def _get_clean_text(self, element):
        return ' '.join(element.stripped_strings) if element else ''

    def _normalize_url(self, url):
        return urljoin(self.base_url, url).split('#')[0]

    def _is_valid_url(self, url):
        parsed = urlparse(url)
        if parsed.netloc != urlparse(self.base_url).netloc:
            return False
        if not parsed.path.startswith('/wiki/'):
            return False
        if ':' in parsed.path.split('/wiki/')[-1]:
            return False
        return parsed.scheme in ['http', 'https']

    def _extract_page_data(self, soup):
        data = {
            'title': self._get_clean_text(soup.find(id='firstHeading')),
            'summary': '',
            'infobox': {},
            'sections': [],
            'categories': [],
            'references': []
        }
        # And Now
        # Extract summary from first paragraph of the damn page
        summary_para = soup.find('div', class_='mw-parser-output').find('p')
        data['summary'] = self._get_clean_text(summary_para)

        # Extract infobox like a boss
        infobox = soup.find('table', class_='infobox')
        if infobox:
            for row in infobox.find_all('tr'):
                th = row.find('th')
                td = row.find('td')
                if th and td:
                    data['infobox'][self._get_clean_text(th)] = self._get_clean_text(td)

        # Extract sections like a pro
        for section in soup.select('.mw-parser-output > h2, .mw-parser-output > h3'):
            data['sections'].append({
                'title': self._get_clean_text(section),
                'content': self._get_clean_text(section.find_next_sibling('p'))
            })

        # Extract categories like a Pimp
        data['categories'] = [
            self._get_clean_text(cat) 
            for cat in soup.select('#mw-normal-catlinks ul li a')
        ]

        # Extract references like a bitch 
        data['references'] = [
            self._get_clean_text(ref) 
            for ref in soup.select('.references li')
        ]

        return data

    def _process_page(self, url):
        try:
            time.sleep(self.request_delay)
            
            if not self._is_allowed(url):
                self.logger.warning(f"URL blocked by robots.txt: {url}")
                return None, []

            response = self.session.get(
                url,
                headers={'User-Agent': self.user_agent},
                timeout=10
            )
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'lxml')
            data = self._extract_page_data(soup)

            # I need to find and normalize internal links
            links = set()
            for link in soup.select('a[href^="/wiki/"]'):
                absolute_url = self._normalize_url(link['href'])
                if self._is_valid_url(absolute_url):
                    links.add(absolute_url)

            return data, list(links)

        except RequestException as e:
            self.logger.error(f"Request failed for {url}: {e}")
            return None, []
        except Exception as e:
            self.logger.error(f"Error processing {url}: {e}")
            return None, []

    def _save_data(self):
        with open(self.output_file, 'a', encoding='utf-8') as f:
            for item in self.data_buffer:
                json.dump(item, f, ensure_ascii=False)
                f.write('\n')
        self.data_buffer = []

    def crawl(self):
        queue = deque([self.start_url])
        queued_urls = {self.start_url}
        page_count = 0

        while queue and page_count < self.max_pages:
            current_url = queue.popleft()
            queued_urls.discard(current_url)

            if current_url in self.visited_urls:
                continue

            self.logger.info(f"Crawling: {current_url}")
            self.visited_urls.add(current_url)

            page_data, new_links = self._process_page(current_url)
            if page_data:
                self.data_buffer.append({
                    'url': current_url,
                    'data': page_data
                })
                page_count += 1

                # data needs to be saved periodically
                if len(self.data_buffer) >= 10:
                    self._save_data()

                # add new links to queue
                for link in new_links:
                    if link not in self.visited_urls and link not in queued_urls:
                        queue.append(link)
                        queued_urls.add(link)

        # final save
        if self.data_buffer:
            self._save_data()

def main():
    parser = argparse.ArgumentParser(description='Wikipedia Web Crawler')
    parser.add_argument('--start-url', type=str, default='https://en.wikipedia.org/wiki/Web_crawler',
                        help='Starting URL for crawling')
    parser.add_argument('--max-pages', type=int, default=100,
                        help='Maximum number of pages to crawl')
    parser.add_argument('--request-delay', type=float, default=1.0,
                        help='Delay between requests in seconds')
    parser.add_argument('--output', type=str, default='wikipedia_data.jsonl',
                        help='Output JSONL file path')
    args = parser.parse_args()

    config = {
        'start_url': args.start_url,
        'max_pages': args.max_pages,
        'request_delay': args.request_delay,
        'output_file': args.output,
        'user_agent': 'WikipediaResearchBot/1.0 (+https://example.com/bot)'
    }

    crawler = WikipediaCrawler(config)
    crawler.crawl()
    

if __name__ == '__main__':
    main()
    
    
