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



my_list = LinkedList()
my_list.insert_node(3)
my_list.insert_node(5)
my_list.insert_node(15)
my_list.insert_node(32)
my_list.insert_node(25)
my_list.insert_node(80)
my_list.insert_node(56)
my_list.display_list()
