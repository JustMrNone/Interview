from collections import Counter

def duplicate_count(text):
    counted = Counter(text.lower())
    thelist = counted.values()
    newlist = [i for i in thelist if i > 1]
    howmanytimes = len(newlist)
    if howmanytimes < 1: 
        return 0
    else:
        return howmanytimes

mystr = "indivisibility"

print(duplicate_count(mystr))


