def solution(text, ending):
    # your code here...
    return True if text[-len(ending):] == ending else False 
print(solution('abc', 'bc'))
 # returns true
solution('abc', 'd') # returns false