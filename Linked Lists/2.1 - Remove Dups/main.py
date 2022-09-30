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

    def remove_Duplicate(self):
        current = self.head    
        prev = None
        mySet = set()

        while current:
            if current.value not in mySet:
                mySet.add(current.value)
                prev = current
            else:
                prev.next = current.next

            current = current.next




my_list = LinkedList()
my_list.insert_node(25)
my_list.insert_node(35)
my_list.insert_node(15)
my_list.insert_node(32)
my_list.insert_node(25)
my_list.insert_node(80)
my_list.insert_node(15)
my_list.display_list()
print("\ncalling remove duplicaes\n")
my_list.remove_Duplicate()
my_list.display_list()