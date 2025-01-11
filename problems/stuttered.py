def accum(st):
    stuttered = []
    for i in range(len(st)):
        stuttered.append(st[i].upper() + st[i].lower() * i)
    ans = '-'.join(stuttered)
    return ans 
print(accum("abcd"))