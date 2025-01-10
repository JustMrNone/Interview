from typing import List
def order(sentence: str) -> str:
  # code here
    mydict: dict = dict()
    numbers: List = list()
    
    mylist: List = sentence.split()

    for i in mylist:
        for j in range(len(i)):
            if i[j].isdigit():
                numbers.append(i[j])
                           
    for k in range(len(numbers)):
        mydict[numbers[k]] = mylist[k]
    
    sorteddict: dict = dict(sorted(mydict.items()))        
    thelist: List = list(sorteddict.values()) 
    thastring: str = ' '.join(thelist)
    return thastring 
                


mystr = "is2 Thi1s T4est 3a"

print(order(mystr))