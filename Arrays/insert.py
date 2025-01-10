arr = [1,0,2,3,0,4,5,0]
res = []

for i in arr:
    if i == 0:
        res.extend([0, 0])
    else:
        res.append(i)

print(res)