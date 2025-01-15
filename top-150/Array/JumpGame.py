from typing import List 

def canJump(nums: List[int]) -> bool:
    maxi = 0
    for i in range(len(nums)):
        if i > maxi:
            return False 
        maxi = max(maxi, i + nums[i])
    return True
        





nums1 = [3,2,1,0,4]
nums2 = [2,3,1,1,4]

print(canJump(nums1))