import re

def is_it(sentence: str) -> bool:
    thestring = ''.join(char.lower() for char in sentence if char.isalnum())
    start = 0
    end = len(thestring) - 1
    
    while start < end:
        if thestring[start] != thestring[end]:
            return False
        
        start += 1
        end -= 1

        return True

def isitPalindrome(sentence: str) -> bool:
    thesentence = re.sub(r'[^a-z0-9]', '', sentence.lower())
    start = 0
    end = len(thesentence) - 1
    while start < end:
        if thesentence[start] != thesentence[end]:
            return False
        start += 1
        end -= 1
        return True 
    
def test_case(ans: bool, expected: bool, error: str = "Error") -> str:
    if ans == expected: 
        return "Passed"
    else:
        return error
    
def main():
    print(is_it("asa"))
    print(is_it("asw"))
    print(is_it("A man, a plan, a canal: Panama")) 
    print(is_it("race a car")) 
    print(is_it("Was it a car or a cat I saw?"))  
    print(test_case(is_it("asa"), True, "Failed, check code"))
    print(test_case(is_it("asasss"), True, "This is an intentional Error"))
    print(test_case(is_it("asasss"), True))    
    print(test_case(is_it("Was it a car or a cat I saw?"), True, "Failed, Something is Wrong"))
    print(isitPalindrome("asa"))
    print(isitPalindrome("Was it a car or a cat I saw?"))
    
if __name__ == "__main__":
    main()