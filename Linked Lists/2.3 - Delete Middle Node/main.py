import math

class Node(object):
    """
    This is a Node class.
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert_node(self, data):
        """
        :param data: Node data
        :return: None
        """
        node = Node(data)
        node.next = self.head
        self.head = node

    def display_list(self):

        current = self.head
        while current:
            print(current.value)
            current = current.next

    def delete_middle_node(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        toBeDeleted = math.ceil(count/2)
        current = self.head

        for i in range(toBeDeleted - 2):
            current = current.next
        print("current\n")
        print(current.value)
        print("\n")
        currentTwo = current
        currentTwo = currentTwo.next
        currentTwo = currentTwo.next
        current.next = currentTwo
        print("second")
        print(currentTwo.value)
        print("\n")




my_list = LinkedList()
my_list.insert_node(7)
my_list.insert_node(6)
my_list.insert_node(5)
my_list.insert_node(4)
my_list.insert_node(3)
my_list.insert_node(2)
my_list.insert_node(1)
my_list.display_list()
print("\ndelete middle node\n")
my_list.delete_middle_node()
my_list.display_list()
