from typing import List 

class Mountain:
    def __init__(self, values: List[int]):
        self.values = values
    
    def isitmountain(self) -> bool:
        lenght = len(self.values)
        count = 0
        
        while count + 1 < lenght and self.values[count] < self.values[count + 1]:
            count += 1
        
        if count == 0 or count == lenght - 1:
            return False 
        
        while count + 1 < lenght and self.values[count] > self.values[count + 1]:
            count += 1
        
        ans = count == lenght - 1
        return ans 
    
def main():
    numbers = input().split()
    myvals = []
    for i in range(len(numbers)):
        myvals.append(int(numbers[i]))
    isit = Mountain(myvals).isitmountain()
    print(isit)

if __name__ == "__main__":
    main()
    
        