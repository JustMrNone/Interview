# my solution 

nums = [8,1,2,2,3]


def count_smalls(numbers):
    ans = []
    for i in range(len(numbers)):
        count = 0
        for j in range(len(numbers)):
            if numbers[j] < numbers[i]:
                count += 1
        ans.append(count)
        count = 0
    return ans   
    
# optimal solution 
def count_smalls_O(numbers):
    temp = sorted(numbers)
    dictt = {}
    ans = []
    
    for index, value in enumerate(temp):
        if value not in dictt:
            dictt[value] = index
    
    for i in numbers:
        ans.append(dictt[i])
    
    return ans 
    
    
# damn that is optimal solution 
def count_smallers(number):
    count = [0] * 102
    
    for num in nums:
        count[num + 1] += 1
    
    for i in range(1, 102):
        count[i] += count[i-1]
    
    return [count[num] for num in nums]


ex1 = count_smalls(nums)
ex2 = count_smallers(nums)
ex3 =  count_smalls_O(nums) 
print(ex1)
print(ex2)   
print(ex3)