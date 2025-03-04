from typing import List 

# Solution 1
mynums = [-4, -1, 0, 3, 10]

def sortedsquared(nums: List[int]) -> int:
    # List comprehension to square each element: O(n)
    squared = [num ** 2 for num in nums]
    
    # Sorting the squared list: O(n log n)
    squared.sort()
    
    # Total time complexity: O(n log n)
    return squared


