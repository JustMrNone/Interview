from typing import List 


# slower 
# time complexity (n * n = O(n ^ 2)) 
def twoSum(nums: List[int], target: int) -> List[int]:
    indexes = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                indexes.extend([i, j])
    return indexes
    




#faster O(N)

def two_sum(nums: List[int] = [2, 11, 7, 15], target: int = 9):
    hash_map = {}
    
    for i, v in enumerate(nums):
        diff = target - v 
        if diff in hash_map:
            return [i, hash_map[diff]]

        hash_map[v] = i


        
        
print(two_sum())