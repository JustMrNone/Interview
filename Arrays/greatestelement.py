from typing import List 

def replaceElements(self, arr: List[int]) -> List[int]:
    
    n = len(arr)
    maxbyfar = -1 
    
    for i in range(n - 1, -1, -1):
        current = arr[i]
        arr[i] = maxbyfar
        maxbyfar = max(current, maxbyfar)
    return arr
    