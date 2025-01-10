from typing import List 


class Mountain:
    def __init__(self, values: List[int]):
        self.values = values 
    def IsitMountain(self) -> bool:
        lenght = len(self.values)
        count = 0
        while count + 1 < lenght and self.values[count] < self.values[count + 1]:
            count += 1
        
        if count == 0 or count == lenght - 1:
            return False 
        
        while count + 1 < lenght and self.values[count] > self.values[count + 1]:
            count += 1
        isitreally = count == lenght - 1
        return isitreally 

def main():
    vals = []
    nums = input().split()
    for i in range(len(nums)):
        vals.append(int(nums[i]))
    ans = Mountain(vals).IsitMountain()
    print(ans)

if __name__ == "__main__":
    main()