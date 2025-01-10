def digitize(n):
    stri = str(n).isdigit()
    return list(stri[::-1])

myint = 35231

print(digitize(myint))

