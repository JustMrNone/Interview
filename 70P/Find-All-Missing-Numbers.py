nums1 = [4,3,2,7,8,2,3,1]

nums2 = [1,1]


def find_all(numbs):
    setn = set(numbs)
    actual_range = range(1, len(numbs))
    ans = []
    for i in actual_range:
        if i not in setn:
            ans.append(i)
            
    return ans


ans = find_all(nums1)
print(ans)