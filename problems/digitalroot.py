def digital_root(n):
    numbers = [int(i) for i in str(n)]
    thesum = sum(numbers)
    while len(str(thesum)) > 1:
        rest = [int(i) for i in str(thesum)]
        thesum = sum(rest)

    return thesum
        
        

print(digital_root(493193))