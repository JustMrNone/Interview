class Phil:
    def __init__(self, x: int):
        self.x = x
    def phili(self) -> bool:
        return str(self.x) == str(self.x)[::-1]

def main() -> None:
    x = int(input())
    ans = Phil(x).phili()
    print(ans)

if __name__ == "__main__":
    main()