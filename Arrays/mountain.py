from typing import List 

class Mountain:
    def __init__(self, arr: List[int]):
        self.arr = arr 
        
    def IsitMountain(self) -> bool:
        if len(self.arr) < 3:
            return False
        
        n = len(self.arr)
        i = 0 
        #finding the index of the peak
        while i + 1 < n and self.arr[i] < self.arr[i + 1]:
            i+=1
            
        if i == 0 or i == n - 1:
            return False
        
        while i + 1 < n and self.arr[i] > self.arr[i + 1]:
            i += 1
        ans = i == n - 1
        return ans
    
def main(): 
    myvals = input().split()

    mylist = []
    for i in range(len(myvals)):
        mylist.append(int(myvals[i]))
    mount = Mountain(mylist)
    final = mount.IsitMountain()
    print(final)

if __name__ == "__main__":
    main()
    