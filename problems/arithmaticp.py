from statistics import mean 



arr = sorted([3,5,1])
diff = 0
different = []
while diff + 1 < len(arr):
    ans = arr[diff] - arr[diff+1]
    different.append(ans)
    diff += 1

isit = mean(different)

if ans == isit:
    print(True)
else:
    print(False)
    
