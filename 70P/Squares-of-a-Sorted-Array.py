from typing import List 
from collections import deque
# Solution 1
mynums = [-4, -1, 0, 3, 10]

def sortedsquared(nums: List[int]) -> int:
    # List comprehension to square each element: O(n)
    squared = [num ** 2 for num in nums]
    
    # Sorting the squared list: O(n log n)
    squared.sort()
    
    # Total time complexity: O(n log n)
    return squared


# solution 2 

def sorted_squares(nums):
    # Edge case: if nums is empty, return empty list
    if not nums:
        return []
    
    # Find the index of the first non-negative number
    first_positive_idx = len(nums)  # default if no non-negative found
    for i, val in enumerate(nums):
        if val >= 0:
            first_positive_idx = i
            break
    
    # Split into two parts:
    # A: non-negative portion
    # B: reversed negative portion turned positive
    A = nums[first_positive_idx:]            # non-negative values
    B = [-1 * n for n in reversed(nums[:first_positive_idx])]  # negatives reversed, made positive
    
    # Merge function: merges two sorted lists into one sorted list
    def merge(arr1, arr2):
        i, j = 0, 0
        merged = []
        
        # Compare elements from both lists and pick smaller
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        
        # Append remaining elements, if any
        if i < len(arr1):
            merged.extend(arr1[i:])
        if j < len(arr2):
            merged.extend(arr2[j:])
        
        return merged
    
    # Merge A and B (which are sorted by absolute value)
    merged_by_abs = merge(A, B)
    
    # Square each value in the merged list
    result = [x**2 for x in merged_by_abs]
    return result

# Example usage:
nums = [-7, -3, -2, 0, 1, 4, 5]
print(sorted_squares(nums))
# Output: [0, 1, 4, 9, 9, 16, 49]


# Two pointers approach to find the squares of a sorted array
# Time complexity: O(n), where n is the length of the input list
# This is more efficient than the O(n log n) complexity of the sortedsquared function
def sortedSquares(nums: List[int]) -> List[int]:
    answer = deque()  # Initialize a deque to store the result
    
    lp = 0  # Left pointer starting at the beginning of the list
    rp = len(nums) - 1  # Right pointer starting at the end of the list
    
    # Iterate until the two pointers meet
    while lp <= rp:
        left = abs(nums[lp])  # Absolute value of the left pointer element
        right = abs(nums[rp])  # Absolute value of the right pointer element
        if left > right:
            answer.appendleft(left * left)  # Append the square of the left element to the front
            lp += 1  # Move the left pointer to the right
        else:
            answer.appendleft(right * right)  # Append the square of the right element to the front
            rp -= 1  # Move the right pointer to the left
    
    listans = list(answer)  # Convert the deque to a list
    return listans  # Return the sorted squares list
    
print(sortedSquares(nums))



"""
The difference in time complexity between inserting at the beginning of an array and using a
`deque.appendleft()` operation comes down to how each data structure handles insertion.

### **1. Inserting at the Beginning of an Array (Python List)**
   - **Time Complexity: \( O(n) \)**  
   - Python lists are implemented as dynamic arrays.  
   - When inserting at the beginning (`list.insert(0, element)`), all existing elements must be shifted one position to the right to make space for the new element.
   - This results in a time complexity of **\( O(n) \)** since shifting elements takes linear time.

### **2. Using `collections.deque.appendleft()`**
   - **Time Complexity: \( O(1) \)**
   - `deque` (double-ended queue) is implemented as a **doubly linked list** or a ring buffer.
   - `appendleft()` adds an element at the beginning without shifting other elements.
   - This results in a constant-time \( O(1) \) operation.

### **Conclusion**
- If you frequently insert elements at the beginning, `deque.appendleft()` is much more efficient (\( O(1) \) vs. \( O(n) \)).
- If you need random access like a list (`arr[i]`), then a list is better despite slower insertions.

"""