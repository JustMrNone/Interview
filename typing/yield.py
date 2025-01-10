
def gen():
    mystring = list("hello") 
    for i in range(len(mystring)):
        mystring[i] *= 2 
    yield ''.join(mystring)
    
    
def generate(n: int = 10):
    for i in range(n + 1):
        yield i
    
      
"""

for num in generate(5):
    print(num)

""" 

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

# Usage
"""gen = infinite_sequence()
for _ in range(2**256):
    print(next(gen))
 """
    
def fibonacci_sequence(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Usage
print(list(fibonacci_sequence(100)))   

    

#variable = list(gen())
#print(variable[0])
