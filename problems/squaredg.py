def square_digits(num):
    mylist = [int(i) ** 2 for i in str(num)]
    thenum = ''.join(str(i) for i in mylist)
    return int(thenum)

print(square_digits(9119))