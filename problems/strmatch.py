from typing import List
from collections import Counter 

def solve(a: List, b: List) -> List:
    ans = []
    myvals = Counter(a)
    for i in range(len(b)):
        if b[i] in myvals.keys():
            ans.append(myvals[b[i]])  
        elif b[i] not in myvals.keys():
            ans.append(0)
        
    return ans 


array1 = ['abc', 'abc', 'xyz', 'cde', 'uvw']
array2 = ['abc', 'cde', 'uap']

print(solve(array1, array2))