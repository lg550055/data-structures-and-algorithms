class Node:
    """ Creates and maintains linked list nodes """
    def __init__(self, value, next_=None): #using _ to differentiate from built in next method
        self.value = value
        self.next = next_

class TargetError(Exception):
    """ handles target errors in LinkedList methods """
    def __str__(self):
        return 'Invalid. Target is either negative or larger than the list'

class LinkedList:
    """ Put docstring here """
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
        s = ''
        current = self.head
        while current:
            s = s + '{ '+ str(current.value) + ' } -> '
            current = current.next
        return s + "NULL"

    def append(self, value):
        """ inserts new node at end of list """
        current = self.head
        while current:
            if current.next == None:
                current.next = Node(value)
                break
            current = current.next
        if not self.head:
            self.head = Node(value)

    def insert_before(self, target, value):
        """ inserts new node before target """
        current = self.head
        if current.value == target:
            self.insert(value)
        else:
            while current.next:
                if current.next.value == target:
                    current.next = Node(value, current.next)
                    break
                current = current.next
            if not current.next:
                return False

    def insert_after(self, target, value):
        """ inserts new node after target """
        current = self.head
        while current:
            if current.value == target:
                current.next = Node(value, current.next)
                break
            current = current.next

    def kth_from_end(self, k):
        """ reads kth value form the end of list """
        possitions = {}
        counter = 0
        current = self.head
        while current:
            counter += 1
            possitions[counter] = current.value
            current = current.next
        if k >= counter or k < 0:
            raise TargetError
        return possitions[counter-k]