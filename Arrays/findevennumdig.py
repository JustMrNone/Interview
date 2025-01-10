from typing import List


class IsItE: 
    def __init__(self, nums: List[int], count: int = 0) -> int:
        self.nums = nums
        self.count = count
    def isiteven(self):
        for i in self.nums:
            numberofdig = len(str(i))
            if numberofdig % 2 == 0:
                self.count += 1
        return self.count
    

def main():
    numbs = [12,345,2,6,7896]
    isitrealy = IsItE(numbs)
    ans = isitrealy.isiteven()
    print(ans)

if __name__ == "__main__":
    main()