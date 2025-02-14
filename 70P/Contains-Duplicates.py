
nums1 = [1,2,3,1]
nums2 = [1,2,3,4]

def contains_duplicates(nums):
    unique = set(nums)
    if len(unique) == len(nums):
        return False
    else:
        return True
    

print(contains_duplicates(nums1))

print(contains_duplicates(nums2))