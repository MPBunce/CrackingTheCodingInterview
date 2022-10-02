from cgitb import small


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


    def partition(self, x):

        current = self.head

        smallerHead = None
        smallerLast = None
        greaterLast = None
        greaterHead = None
        equalHead = None
        equalLast = None

        while(current != None):

            if(current.value == x):

                if(equalHead == None):
                    equalHead = equalLast = current
                else:
                    equalLast.next = current
                    equalLast = equalLast.next

            elif(current.value < x):
                
                if(smallerHead == None):
                    smallerLast = smallerHead = current
                else:
                    smallerLast.next = current
                    smallerLast = current
            
            else:
                if (greaterHead == None):
                    greaterLast = greaterHead = current
                else:
                    greaterLast.next = current
                    greaterLast = current
            
            current = current.next
                
        if (greaterLast != None) :
            greaterLast.next = None
    
        # Connect three lists
    
        # If smaller list is empty
        if (smallerHead == None) :
        
            if (equalHead == None) :
                self.head = greaterHead
            equalLast.next = greaterHead
            self.head = equalHead
        
        # If smaller list is not empty
        # and equal list is empty
        if (equalHead == None) :
        
            smallerLast.next = greaterHead
            self.head = smallerHead
        
        # If both smaller and equal list
        # are non-empty
        smallerLast.next = equalHead
        equalLast.next = greaterHead
        self.head = smallerHead


my_list = LinkedList()
my_list.insert_node(3)
my_list.insert_node(2)
my_list.insert_node(5)
my_list.insert_node(2)
my_list.insert_node(3)
my_list.insert_node(4)
my_list.insert_node(1)
my_list.display_list()

print("\nPartition:\n")
my_list.partition(3)

my_list.display_list()
