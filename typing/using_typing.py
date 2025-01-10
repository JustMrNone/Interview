from collections.abc import Iterator

#string: str = input()
#print(string[::-1])

def gen(n: int) -> Iterator[int]:
    i = 0
    while i < n:
        yield i
        i += 1
    
num = 100
print(list(gen(num)))