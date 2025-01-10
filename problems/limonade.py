from typing import List

def lemonadeChange(bills: List[int]) -> bool:
    # Initialize counters for $5 and $10 bills
    five_count = 0
    ten_count = 0
    
    for bill in bills:
        if bill == 5:
            five_count += 1
        elif bill == 10:
            if five_count == 0:
                return False 
            five_count -= 1
            ten_count += 1
        elif bill == 20:
            if five_count > 0 and ten_count > 0:
                five_count -= 1
                ten_count -= 1
            elif five_count >= 3:
                five_count -= 3
            else:
                return False 
    return True    

# Test cases
billss = [5, 5, 10, 10, 10, 20]
print(lemonadeChange(billss))  # Output should be False

billss2 = [5, 5, 5, 10, 20]
print(lemonadeChange(billss2))  # Output should be True