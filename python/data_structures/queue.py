import re
from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Queue:
    """ Allows read and delete only from the front, insert only into the end """

    def __init__(self):
        """ Creates an empty queue when instantiated """
        self.front = None
        self.end = None

    def enqueue(self, value):
        """ Adds new node to the end of the queue """
        if self.is_empty():
            self.front = self.end = Node(value)
        else:
            new_node = Node(value)
            self.end.next = new_node
            self.end = new_node

    def dequeue(self):
        """ Removes the node from the front of the queue """
        if self.is_empty():
            raise InvalidOperationError
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError
        else:
            return self.front.value

    def is_empty(self):
        return not self.front
