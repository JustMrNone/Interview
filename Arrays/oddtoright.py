from typing import List 

def sortArrayByParity(nums: List[int]) -> List[int]:
    left = 0
    right = len(nums) - 1
    
    while left < right:
        # Find odd number from left
        while left < right and nums[left] % 2 == 0:
            left += 1
        # Find even number from right
        while left < right and nums[right] % 2 == 1:
            right -= 1
        # Swap when both found
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
    
    return nums

mylist = [3,1,2,4]
print(sortArrayByParity(mylist))