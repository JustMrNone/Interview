# Define the Node class
class Node:
    def __init__(self, data):
        """
        Initialize a new node with data and a pointer to the next node.
        :param data: The value to store in the node.
        """
        self.data = data  # Store the value
        self.next = None  # Initialize the next pointer to None (end of the list)

# Define the LinkedList class
class LinkedList:
    def __init__(self):
        """
        Initialize the linked list. Start with an empty list (head is None).
        """
        self.head = None  # The head node of the list

    def is_empty(self):
        """
        Check if the linked list is empty.
        :return: True if the list is empty, False otherwise.
        """
        return self.head is None

    def append(self, data):
        """
        Add a new node with the specified data to the end of the list.
        :param data: The value to add to the list.
        """
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = new_node
            return
        # Otherwise, traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next  # Move to the next node
        current.next = new_node  # Link the last node to the new node

    def prepend(self, data):
        """
        Add a new node with the specified data to the beginning of the list.
        :param data: The value to add to the list.
        """
        new_node = Node(data)  # Create a new node with the given data
        new_node.next = self.head  # Point the new node to the current head
        self.head = new_node  # Update the head to the new node

    def delete(self, key):
        """
        Delete the first node with the specified value (key).
        :param key: The value to delete from the list.
        """
        current = self.head
        # Case 1: The head node contains the key
        if current and current.data == key:
            self.head = current.next  # Update the head to the next node
            current = None  # Remove the old head node
            return
        # Case 2: The key is somewhere else in the list
        prev = None
        while current and current.data != key:
            prev = current  # Keep track of the previous node
            current = current.next  # Move to the next node
        if current is None:
            # If the key was not found in the list
            return
        prev.next = current.next  # Unlink the node from the list
        current = None  # Delete the node

    def display(self):
        """
        Print the elements of the linked list.
        """
        elements = []  # Create a list to store node values
        current = self.head  # Start from the head node
        while current:
            elements.append(current.data)  # Add the current node's data to the list
            current = current.next  # Move to the next node
        print(" -> ".join(map(str, elements)))  # Display the elements as a string

    def find(self, key):
        """
        Search for a node with the specified value.
        :param key: The value to search for.
        :return: True if the value is found, False otherwise.
        """
        current = self.head  # Start from the head node
        while current:
            if current.data == key:  # If the value is found
                return True
            current = current.next  # Move to the next node
        return False  # Value not found

    def reverse(self):
        """
        Reverse the linked list.
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Save the next node
            current.next = prev  # Reverse the link
            prev = current  # Move the 'prev' pointer forward
            current = next_node  # Move the 'current' pointer forward
        self.head = prev  # Update the head to the new first node

# Example usage of the LinkedList class
if __name__ == "__main__":
    # Create an empty linked list
    ll = LinkedList()

    # Append elements to the list
    ll.append(10)
    ll.append(20)
    ll.append(30)

    # Display the list
    ll.display()  # Output: 10 -> 20 -> 30

    # Prepend an element to the list
    ll.prepend(5)
    ll.display()  # Output: 5 -> 10 -> 20 -> 30

    # Delete an element from the list
    ll.delete(20)
    ll.display()  # Output: 5 -> 10 -> 30

    # Search for an element in the list
    print(ll.find(10))  # Output: True
    print(ll.find(40))  # Output: False

    # Reverse the list
    ll.reverse()
    ll.display()  # Output: 30 -> 10 -> 5

    # Check if the list is empty
    print(ll.is_empty())  # Output: False
