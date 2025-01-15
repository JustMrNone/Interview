from typing import List 

def rotate(nums: List[int], k: int) -> None:
        nums[:] = nums[-k:] + nums[:k]
    



nums = [1,2,3,4,5,6,7]

print(rotate(nums, 3))
