from typing import List 


class Zeroes:
    def __init__(self, values: List[int]):
        self.values = values 
    
    def zerotoside(self):
        length = len(self.values)
        notzero = 0
        
        for i in range(length):
            if self.values[i] != 0:
                self.values[notzero] = self.values[i]
                notzero += 1
        for i in range(notzero, length):
            self.values[i] = 0
        
        return self.values
    
def main():
    nums = [0, 1, 0, 3, 12]
    initi = Zeroes(nums).zerotoside()
    print(initi)
 

main()