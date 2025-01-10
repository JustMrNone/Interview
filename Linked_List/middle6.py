from typing import List, NoReturn


class Node:
    def __init__(self, data: int = 0, next = None):
        self.data = data 
        self.next = next 
    
class Find:
    def __init__(self, head: Node):
        self.slow = head 
        self.fast = head 
        
    def middlefind(self) -> Node:
        while self.fast and self.fast.next:
            self.slow = self.slow.next 
            self.fast = self.fast.next.next 
        
        return self.slow 


def main() -> NoReturn:
    intake = list(input())
    myvals = list(map(int, intake))
    mynode = helper(myvals)
    ans = Find(mynode).middlefind()
    print(ans.data)  
    
    
def helper(values: List) -> Node:
    head = Node(values[0])
    cur = head 
    for value in values[1:]:
        cur.next = Node(value)
        cur = cur.next 
    return head 

if __name__ == "__main__":
    main()  