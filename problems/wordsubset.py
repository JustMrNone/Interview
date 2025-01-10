from typing import List

def wordSubsets(words1: List[str], words2: List[str]) -> List[str]:
    required_chars = ''.join(words2)
    exists = []
    for word in words1:
        if all(char in word for char in required_chars):
            exists.append(word)
    return exists

# Test cases
wordsa = ["amazon", "apple", "facebook", "google", "leetcode"]
wordsb = ["e", "o"]

print(wordSubsets(wordsa, wordsb))  # Output should be ["facebook", "google", "leetcode"]