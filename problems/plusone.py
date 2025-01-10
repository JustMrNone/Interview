from typing import List 

def plusOne(digits: List[int]) -> List[int]:
        digit = int("".join(map(str, digits)))
        digitplus = digit + 1
        stringed = str(digitplus)
        anslist = []
        for i in range(len(stringed)):
            anslist.append(stringed[i])
            
        answ = list(map(int, anslist))
        return answ
            
#TODO
mylist = [1, 2, 3]
ans = plusOne(mylist)
print(ans)