from collections import Counter 

myarr = [17, 17, 3, 17, 17, 17, 17]

def stray(arr):
    myvar = Counter(arr)
    for key, pair in myvar.items():
        if pair == 1:
            return key
        
print(stray(myarr))