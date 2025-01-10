def digital_root(n):
    while n > 10:
        z = str(n)
        nums = [int(digit) for digit in z]
        return sum(nums)
        
        
n = 24

x = digital_root(n)
print(x)

def digital_root(n):
    while n >= 10:  # Continue while n has more than one digit
        digits = str(n)
        numbers = [int(digit) for digit in digits]
        n = sum(numbers)  # Sum the digits of n
    return n  # Return the final single-digit result
