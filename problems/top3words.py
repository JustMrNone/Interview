import re
from collections import Counter

def top_3_words(text):
    # Use regex to match words including apostrophes
    words = re.findall(r"[a-zA-Z']+", text.lower())
    
    # Filter out invalid words with only apostrophes
    valid_words = [word for word in words if re.search(r"[a-zA-Z]", word)]
    
    # Count the frequency of each word
    word_counts = Counter(valid_words)
    
    # Return the top 3 words based on frequency
    return [word for word, _ in word_counts.most_common(3)]

# Examples
example_1 = """
In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.
"""
print(top_3_words(example_1))  # Output: ["a", "of", "on"]

example_2 = "e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"
print(top_3_words(example_2))  # Output: ["e", "ddd", "aa"]

example_3 = "  //wont won't won't"
print(top_3_words(example_3))  # Output: ["won't", "wont"]
