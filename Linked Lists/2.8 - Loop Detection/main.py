from socket import NI_NUMERICSERV
from tkinter import W


class Node:
  
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
  
  
# Linked List class contains a Node object
class LinkedList:
  
    # Function to initialize head
    def __init__(self):
        self.head = None
  
    def Detect_Loop(self):
        slow, fast = self.head, self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

# Start with the empty list
my_list = LinkedList()
my_list.head = Node(1)
second = Node(2)
my_list.head.next = second
third = Node(3)
second.next = third
fourth = Node(4)
third.next = fourth
fifth = Node(5)
fourth.next = fifth
sixth = Node(6)
fifth.next = sixth
seventh = Node(7)
sixth.next = seventh
eight = Node(8)
seventh.next = eight
nine = Node(9)
eight.next = nine
nine.next = sixth

value = my_list.Detect_Loop()

print("Is there a loop? (T or F):")
print(value)