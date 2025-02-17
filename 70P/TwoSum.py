from typing import list 
# slower 
# time complexity (n * n = O(n ^ 2)) 
def twoSum(nums: List[int], target: int) -> List[int]:
    indexes = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                indexes.extend([i, j])
    return indexes
    



from typing import List 

#faster O(N)

def two_sum(nums: List[int] = [2, 11, 7, 15], target: int = 9):
    hash_map = {}
    
    for index, value in enumerate(nums):
        diff = target - value
        if diff in hash_map:
            ans = [index, hash_map[diff]]
            return ans 
        
        hash_map[value] = index
        
        
print(two_sum())