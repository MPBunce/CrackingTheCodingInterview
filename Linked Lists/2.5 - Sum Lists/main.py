class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert_node(self, data):

        node = Node(data)
        node.next = self.head
        self.head = node

    def display_list(self):

        current = self.head
        while current:
            print(current.value)
            current = current.next


def sumLists(listOne, listTwo):

    stringOne = []
    stringTwo = []
    currentOne = listOne.head
    currentTwo = listTwo.head

    valOne = 1
    while currentOne:
        
        stringOne.append(currentOne.value * valOne)
        currentOne = currentOne.next
        valOne = valOne *10

    valTwo = 1
    while currentTwo:
        
        stringTwo.append(currentTwo.value * valTwo)
        currentTwo = currentTwo.next
        valTwo = valTwo *10

    sumOne = sum(stringOne)
    sumTwo = sum(stringTwo)

    reversedOne = str(sumOne)[::-1]
    reversedTwo = str(sumTwo)[::-1] 

    sumOne = int(reversedOne)
    sumTwo = int(reversedTwo)
    total = sumOne + sumTwo
    total = str(total) 
    total_list = []

    for char in total:
        total_list.append(char)
    
    
    returned_linked_list = LinkedList()
    for char in total_list:
        val = int(char)
        returned_linked_list.insert_node(val)

    return returned_linked_list

print("List One:\n")
my_list_one = LinkedList()
my_list_one.insert_node(7)
my_list_one.insert_node(1)
my_list_one.insert_node(6)
my_list_one.display_list()
print("\nList Two:\n")
my_list_two = LinkedList()
my_list_two.insert_node(5)
my_list_two.insert_node(9)
my_list_two.insert_node(2)
my_list_two.display_list()
Da_return = sumLists(my_list_one, my_list_two)
print("\nSum Lists Result:\n")
Da_return.display_list()