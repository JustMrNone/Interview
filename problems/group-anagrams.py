from typing import List, NoReturn
from collections import defaultdict

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    
    anagrams = defaultdict(list)
    
    for word in strs:
        # Sort the characters of the word to form the key
        sorted_word = ''.join(sorted(word))
        # Group the anagrams using the sorted word as the key
        anagrams[sorted_word].append(word)
    
    # Return the grouped anagrams as a list of lists
    return list(anagrams.values())

def main() -> NoReturn:
    
# Test cases
    strss = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strss))  # Output should be [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]



main()