def square_root_newton(x, precision=0.0001):
    if x < 0:
        return None  # Square root of a negative number is not real
    
    guess = x / 2 if x >= 1 else x  # Initial guess
    while True:
        new_guess = (guess + x / guess) / 2
        if abs(new_guess - guess) < precision:
            return new_guess
        guess = new_guess

def square_root_binary_search(x, precision=0.0001):
    if x < 0:
        return None  # Square root of a negative number is not real
    
    low, high = 0, max(1, x)
    while high - low > precision:
        mid = (low + high) / 2
        if mid * mid < x:
            low = mid
        else:
            high = mid
    return (low + high) / 2

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 0:
            return 0
        guess = x / 2 if x >= 1 else x
        while True:
            new_guess = (guess + x / guess) / 2
            if abs(new_guess - guess) < 0.0001:
                break
            guess = new_guess

        result = int(new_guess)
        if result * result > x:
            result -= 1

        return result