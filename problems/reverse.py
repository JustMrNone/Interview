
def reverse(x: int) -> int:
    z = list(str(x))
    
    if z[0] == '-':
        z.remove("-")
        z.append("-")
        ans = int(''.join(z[::-1]))
    else:
        ans = int(''.join(z[::-1]))
    
    if ans < -2**31 or ans > 2**31 - 1:
        return 0
    
    return ans 

    
    
    

y = 123
print(reverse(y))