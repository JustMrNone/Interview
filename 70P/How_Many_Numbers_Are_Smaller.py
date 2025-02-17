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

ex1 = count_smalls(nums) 
print(ex1)     
    
# optimal solution 
def count_smalls_O(numbers):
    temp = sorted(numbers)
    
    mydict = {}
    
    for index, number in enumerate(temp):
        if number not in mydict:
            mydict[number] = index
    ans = []
    for i in numbers:
        ans.append(mydict[i])
        
    return ans
    