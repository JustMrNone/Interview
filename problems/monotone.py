"""

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        incre = all(nums[i] <= nums[i+1] for i in range(len(nums) - 1))
        decre = all(nums[j] >= nums[j+1] for j in range(len(nums) - 1))
        ans = incre or decre 
        return ans  
        
"""

"""
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        incre = True
        decre = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                incre = False
            if nums[i] < nums[i + 1]:
                decre = False
        return incre or decre
"""