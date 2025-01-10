def get_middle(s):
    length = len(s)
    if length % 2 != 0:
        index = length // 2
        print(s[index])
    elif length % 2 == 0:
        index = length // 2
        print(s[index - 1: index + 1])

def getmiddle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]


mystr = "he2l3ooo"
get_middle(mystr)
print(getmiddle(mystr))


