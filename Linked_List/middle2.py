from typing import List 


class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
class isitm:
    def middlenode(self, head: Node) -> Node:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        return slow
    
def helper(values: List) -> Node:
    if not values:
        return None
    head = Node(values[0])
    cur = head
    for value in values:
        cur.next = Node(value)
        cur = cur.next 
    return head

def main():
    vals = [1, 2, 3, 4, 5, 6]
    turntolinked = helper(vals)
    whichone = isitm()
    thisone = whichone.middlenode(turntolinked)
    ans = thisone.val
    print(ans)
    
if __name__ == "__main__":
    main()


        