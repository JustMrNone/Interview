def removeit(sen: str) -> str:
    vowels = "aeiouAEIOU"
    removed = [char for char in sen if char not in vowels]
    ans = ''.join(removed)
    return ans 


print(removeit("hi bitch"))
