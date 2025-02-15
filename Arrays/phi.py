

def is_it(mystring):
    thestr = mystring.lower()
    start = 0
    end = len(mystring) - 1
    while start < end:
        if thestr[start] != thestr[end]:
            return False
        start += 1
        end -= 1
    
    return True


ex1 = is_it("Radar")
ex2 = is_it("civic")
ex3 = is_it("today")


print(ex1, ex2, ex3)
    