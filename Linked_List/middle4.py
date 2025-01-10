from typing import List 

class Node:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next 
    
class MiddleNode:
    def ismiddle(self, head: Node) -> Node:
        slow = head 
        fast = head 
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next 
        return slow 
    


def helper(values: List) -> Node:
    if not values:
        return None 
    
    head = Node(values[0])
    cur = head 
    for value in values[1:]:
        cur.next = Node(value)
        cur = cur.next 
    return head 

def main():
    userinput = input().split()
    mylist = []
    for i in range(len(userinput)):
        mylist.append(int(userinput[i]))
    makenode = helper(mylist)
    middlenode = MiddleNode()
    damnitisit = middlenode.ismiddle(makenode)
    print(damnitisit.data)

if __name__ == "__main__":
    main()
        
        
        