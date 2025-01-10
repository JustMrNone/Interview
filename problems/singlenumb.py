from collections import Counter 
from typing import List


def singleNumber(nums: List[int]) -> int:
    counted = Counter(nums)
    
    single = []
    for key, pair in counted.items():
        if pair < 2:
            single.append(key)
    ans = single[0]
    return ans
    

numbs = [4,1,2,1,2]
print(singleNumber(numbs))