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
  
def intersect(listOne, listTwo):
    currentOne = listOne.head
    nums = set()
    while currentOne:
        nums.add(currentOne.data)
        currentOne = currentOne.next

    currentTwo = listTwo.head
    while currentTwo:
        if currentTwo.data in nums:
            return currentTwo.data
        currentTwo = currentTwo.next

    return False



# Start with the empty list
my_list_one = LinkedList()
my_list_one.head = Node(1)
second = Node(2)
my_list_one.head.next = second
third = Node(3)
second.next = third
fourth = Node(4)
third.next = fourth
fifth = Node(5)
fourth.next = fifth
fifth.next = None

my_list_two = LinkedList()
my_list_two.head = Node(6)
seventh = Node(7)
my_list_two.head.next = seventh
eight = Node(8)
seventh.next = eight
nine = Node(9)
eight.next = nine
nine.next = fourth

value = intersect(my_list_one, my_list_two)
print("Where do they intersect?:")
print(value)