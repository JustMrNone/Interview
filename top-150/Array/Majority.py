from collections import Counter 
from typing import List 


def Major(numbers: List[int]) -> int:
    counted = Counter(numbers)
    
    keys = [val for _, val in counted.items()]
    howmany = max(keys)
    for key, pair in counted.items():
        if pair == howmany:
            return key
    

nums = [1,1,1,2,2,3]
print(Major(nums))



