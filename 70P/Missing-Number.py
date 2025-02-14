from typing import List


def missing_numbers(nums: List[int]) -> int:
    return sum(range(len(nums) + 1)) - sum(nums)
    

list1 = [1, 2, 3]
list2 = [3,0,1]
list3 = [0,1]
list4 = [9,6,4,2,3,5,7,0,1]


ans = missing_numbers(list2)
print(ans)