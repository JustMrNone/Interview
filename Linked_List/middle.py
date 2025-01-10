from typing import List


class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next 
        
class middleNode:
    def __init__(self, head: Node):
        self.slow = head
        self.fast = head
    def ans(self) -> Node:
        while self.fast and self.fast.next:
            self.slow = self.slow.next
            self.fast = self.fast.next.next
        return self.slow
    
    
def createlinked(values: List) -> Node:
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head


def main():
    vals = [1,2,3,4,5,6]
    head = createlinked(vals)
    middle = middleNode(head)
    answ = middle.ans()
    print(answ.val)

if __name__ == "__main__":
    main()