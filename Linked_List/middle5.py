from typing import List, NoReturn

class Node:
    def __init__(self, data: int = 0, next = None):
        self.data = data 
        self.next = next 

class is_itmiddle:
    def __init__(self, head: Node):
        self.slow = head 
        self.fast = head 
    
    def ans(self) -> Node:
        while self.fast and self.fast.next:
            self.slow = self.slow.next
            self.fast = self.fast.next.next 
        return self.slow
    
def turntolist(values: List) -> Node:
    head = Node(values[0])
    cur = head
    for value in values[1:]:
        cur.next = Node(value)
        cur = cur.next 
    return head 

def main() -> NoReturn:
    vals = [1,2,3,4,5]
    mylinked = turntolist(vals)
    
    initial = is_itmiddle(mylinked).ans()
    print(initial.data)

if __name__ == "__main__":
    main()
    
    
        
        
    