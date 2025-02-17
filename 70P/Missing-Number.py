from typing import List
import time


#fast 3ms
def missing_numbers(nums: List[int]) -> int:
    return sum(range(len(nums) + 1)) - sum(nums)
    

#slow 

def missing_numbers_slow(nums: List[int]) -> int:
    for i in range(len(nums) + 1):
        if i not in nums:
            return i;
        
        
        
        
list1 = [1, 2, 3]
list2 = [3,0,1]
list3 = [0,1]
list4 = [9,6,4,2,3,5,7,0,1]


ans = missing_numbers(list2)
ans_slow = missing_numbers_slow(list2)
print(ans)
print(ans_slow)
start = time.time()
ans = missing_numbers(list2)
end = time.time()
print(f"Result: {ans}, Time taken: {end - start:.6f} seconds")

# Measure time for missing_numbers_slow
start = time.time()
ans_slow = missing_numbers_slow(list2)
end = time.time()
print(f"Result: {ans_slow}, Time taken: {end - start:.6f} seconds")