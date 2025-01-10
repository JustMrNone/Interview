from typing import List

def arraySign(nums: List[int]) -> int:
    summ = sum(nums)
    if summ > 0:
        return 1
    if summ < 0:
        return -1
    else:
        return 0        

mylist = [1, 2, -8]
print(arraySign(mylist))