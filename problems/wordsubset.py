from typing import List
from collections import Counter

def wordSubsets(words1: List[str], words2: List[str]) -> List[str]:
    # Helper function to count the maximum occurrences of each character in words2
    def count_max_chars(words: List[str]) -> Counter:
        max_count = Counter()
        for word in words:
            word_count = Counter(word)  # Count characters in the current word
            for char in word_count:
                # Update max_count to have the maximum count of each character across all words
                max_count[char] = max(max_count[char], word_count[char])
        return max_count
    
    # Get the maximum character counts required from words2
    required_chars = count_max_chars(words2)
    
    result = []
    for word in words1:
        word_count = Counter(word)  # Count characters in the current word from words1
        # Check if the current word contains at least the required number of each character
        if all(word_count[char] >= required_chars[char] for char in required_chars):
            result.append(word)  # If it does, add it to the result list
    
    return result

# Test cases
wordsa = ["amazon", "apple", "facebook", "google", "leetcode"]
wordsb = ["e", "o"]

print(wordSubsets(wordsa, wordsb))  # Output should be ["facebook", "google", "leetcode"]