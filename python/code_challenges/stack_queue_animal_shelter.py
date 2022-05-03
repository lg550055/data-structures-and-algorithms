from data_structures.stack import Stack


class AnimalShelter:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, animal):
        self.stack1.push(animal)

    def dequeue(self, pref):
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        while not self.stack2.is_empty():
            if self.stack2.peek().value == pref:
                return self.stack2.pop()
            elif not self.stack2.is_empty():
                self.stack1.push(self.stack2.pop())
        return


class Dog():
    def __init__(self):
        self.value = 'dog'


class Cat():
    def __init__(self):
        self.value = 'cat'
