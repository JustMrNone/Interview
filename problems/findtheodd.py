from collections import Counter

mylist = [1,2,2,3,3,3,4,3,3,3,2,2,1]

counted = Counter(mylist)
for k, v in counted.items():
    if v % 2 != 0:
        print(k)
        
print(counted)