def open_or_senior(data):
    ans = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            if i[1] <= -2 or i[1] >= 26:
                return False
            ans.append("Senior")
        else:
            ans.append("Open")
    return ans  
            
    
    
intake =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]



print(open_or_senior(intake))

"""
def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]
"""