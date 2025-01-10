from typing import List

"""
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.

"""

def calPoints(operations: List[str]) -> int:
    stack = []
    for operation in operations:
        if operation == "C":
            stack.pop()
        elif operation == "D":
            stack.append(stack[-1] * 2)
        elif operation == "+":
            stack.append(stack[-1] - stack[-2])
        else:
            stack.append(int(operation))
    ans = sum(stack)
    return ans 

# Example usage
ops = ["5","-2","4","C","D","9","+","+"]
print(calPoints(ops))  # Output should be 27