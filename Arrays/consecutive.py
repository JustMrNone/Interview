
class Consecutive:
    def __init__(self, nums: int, cur: int = 0, mx: int = 0):
        self.nums = nums
        self.cur = cur
        self.mx = mx
        
    def cal(self) -> int:
        for i in self.nums:
            if i == 1:
                self.cur += 1
                self.mx = max(self.mx, self.cur)
            else:
                self.cur = 0
        return self.mx


def main():
    numbers = [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    isit = Consecutive(numbers)
    ans = isit.cal()
    print(ans)

if __name__ == "__main__":
    main()
