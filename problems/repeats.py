#fast 
'''a = input()
b = input()
newval = (a + a)[1:-1]

if b in newval:
    print(True)
else:
    print(False)'''
#fancy 
    
class IsIn:
    def __init__(self, value1: int, value2: int) -> None:
            self.value1 = value1 
            self.value2 = value2
        
    def isitinit(self) -> bool:
        newval = (self.value1 + self.value1)[1:-1]
        if self.value2 in newval:
            return True
        else:
            return False

def main() -> None:
    a = input()
    b = input()
    initis = IsIn(a, b) 
    isitreally = initis.isitinit()
    print(isitreally)

if __name__ == "__main__":
    main()