#recursion 

def persistence(n, steps: int = 0) -> int:
    if n < 10:
        return steps 
    
    mylist = [int(i) for i in str(n)]
    val = 1
    for i in mylist:
        val *= i
    return persistence(val, steps + 1)


print(persistence(999))


"""
LOOP
def persistence(n):
    steps = 0
    while n >= 10:
        product = 1  # Use a separate variable for the product
        for digit in str(n):
            product *= int(digit)
        n = product  # Update n after calculating the product
        steps += 1
    return steps
    

"""