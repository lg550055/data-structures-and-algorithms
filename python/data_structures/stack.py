from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Stack:
    """ Allows read, write and delete only from the top """

    def __init__(self):
        """ Creates an empty Stack when instantiated """
        self.top = None

    def push(self, value):
        """ adds a new node to the top of the stack"""
        try:
            self.top = Node(value, self.top)
        except InvalidOperationError:
            self.top = Node(value)

    def pop(self):
        try:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
        except AttributeError:
            raise InvalidOperationError

    def peek(self):
        try:
            return self.top.value
        except AttributeError:
            raise InvalidOperationError

    def is_empty(self):
        return self.top is None

