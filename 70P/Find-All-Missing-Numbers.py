"""
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

"""
# the solution is in O(n)

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

def find_all_O1(numbs):
    for i in range(len(numbs)):
        temp = abs(numbs[i]) - 1
        if numbs[temp] > 0:
            numbs[temp] *= -1
    
    res = []
    for i, n in enumerate(numbs):
        if n > 0:
            res.append(i+1)
            
    return res


print(find_all_O1(nums1))
            
