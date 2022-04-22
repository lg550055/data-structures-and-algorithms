class Node:
    """ Creates and maintains linked list nodes """
    def __init__(self, value, next_=None): #using _ to differentiate from built in next method
        self.value = value
        self.next = next_

class LinkedList:
    """
    Put docstring here
    """
    def __init__(self):
        self.head = None

    def insert(self, value):
        """ inserts new head node """
        # pass the old head as the next property of the inserted node
        self.head = Node(value, self.head)

    def includes(self, target):
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
        return False

    def __str__(self):
        pass