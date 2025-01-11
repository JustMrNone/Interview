class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return 
        
        current = self.head 
        while current.next:
            current = current.next
        current.next = newNode
        
    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def delete(self, key):
        current = self.head
        if current and current.data != key:
            prev = current 
            current = current.next 
        if current is None:
            return 
        prev.next = current.next
        current = None
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
         
        print("->".join(map(str, elements)))    
    
    def find(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next 
        return False
    
    def reverse(self):
        prev = None
        current = self.head 
        while current:
            nextNode = current.next 
            current.next = prev
            prev = current 
            current = nextNode
        self.head = prev
    
def main():
    Linked_List = LinkedList()

    print("Add the Value, ctrl-z to continue")
    
    while True:
        try:
            myval = int(input(":"))
            Linked_List.append(myval)
        except EOFError:
            break 
    
    print("prepend if you want, ctrl-z to continue")
    
    while True:
        try:
            myval = int(input(':'))
            if myval:
                Linked_List.prepend(myval)
        except EOFError:
            break
        
    answ = input("reverse\n(y/n):").lower()
    if answ == 'y':
        Linked_List.reverse()
        
    theans = input("Find A value?\n(y/n):").lower()
    if theans == 'y': 
        myval = int(input(":"))
        if Linked_List.find(myval):
            print(f"{myval} is in the Linked List")
        else:
            print(f"{myval} is not in fact in the Linked List")


    print("Your Linked List:")
    Linked_List.display() 


if __name__ == "__main__":
    main()