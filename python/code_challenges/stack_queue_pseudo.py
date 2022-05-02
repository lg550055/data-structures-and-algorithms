from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, value):
        self.s1.push(value)

    def dequeue(self):
        if self.s1.is_empty() and self.s2.is_empty():
            raise Exception
        elif self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
            return self.s2.pop()
        else:
            return self.s2.pop()