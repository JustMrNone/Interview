
def is_pangram(st):
    # Define the alphabet as a set
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    # Convert the string to lowercase, remove non-alphabetic characters, and convert to a set
    filtered_chars = set(c for c in st.lower() if c.isalpha())
    # Check if the filtered characters include all the alphabet letters
    return filtered_chars == alphabet

strint = "The quick brown fox jumps over the lazy dog".lower().replace(" ", "")

print(is_pangram(strint))


"""
def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True
    
"""