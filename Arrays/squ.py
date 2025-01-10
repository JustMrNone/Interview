nums = [-7,-3,2,3,11]
res = []
for i in range(len(nums)):
    res.append(nums[i] ** 2)
res.sort()
print(res)