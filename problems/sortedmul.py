from typing import List 

def comp(array1: List, array2: List) -> bool:
    # your code
    if len(array1) != len(array2):
        return False
    
    array1.sort() 
    array2.sort()
    for i in range(len(array1)):
        if array1[i] ** 2 != array2[i]:
            return False
    return True

    
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

ans = comp(a, b)

print(ans)