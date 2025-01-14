from typing import List 
from collections import Counter


def removeDuplicates(nums: List[int]) -> int:
        """
        look for the elements that are more than 2 
        only leave two        
        """
        counted = Counter(nums)
        
        for key, pair in counted.items():
            if pair > 2:
                howmany = pair - 2
                for _ in range(howmany):
                    nums.remove(key)
                
        return nums
    

numss = [1,1,1,2,2,3]
new = removeDuplicates(numss)
print(new)

    
    