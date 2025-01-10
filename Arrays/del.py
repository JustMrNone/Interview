from typing import List

def removeElement(nums: List[int], val: int) -> int:
        nums[:] = [i for i in nums if i != val]
        return nums
        
                
                

mylist = [3,2,2,3]
vall = 3

ans = removeElement(mylist, vall)

print(ans)