from typing import List 


class Node:
    def __init__(self, val: int = 0, next = None):
        self.val = val 
        self.next = next 
        
        
class middle:
    def __init__(self, head: List):
        self.head = head

    def middle(self, values: Node) -> Node:
        slow = values
        fast = values
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def helper(self) -> Node:
        if not self.head:
            return None
        head = Node(self.head[0])
        cur = head 
        for value in self.head[1:]:
            cur.next = Node(value)
            cur = cur.next 
        return head 
    
def main():
    vals = [1, 2, 3, 4 ,5, 6, 7, 8, 9, 10]
    middleinit = middle(vals)
    newval = middleinit.helper()
    ans = middleinit.middle(newval)
    print(ans.val)

if __name__ == "__main__":
    main()
    
    
            
        