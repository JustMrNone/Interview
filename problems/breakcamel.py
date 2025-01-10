def solution(s: str) -> str:
    x = []
    for i in range(len(s)):
        if s[i].islower():
            x.append(s[i])
        if s[i].isupper(): 
            x.append(" ")
            x.append(s[i])
    ans = ''.join(x)
    return ans 
        
myans = solution("assHole")
print(myans)

