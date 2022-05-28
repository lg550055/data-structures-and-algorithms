from data_structures.linked_list import LinkedList

class Hashtable:
    """ Hash table with set, get, contains, keys and hash methods """

    def __init__(self, size=512):
        self.size = size
        self.arr = [None] * size


    def hash(self, key):
        """ Returns the index corresponding to the key """
        return (sum([ord(e) for e in key]) * 93) % self.size


    def set(self, key, value):
        """ Adds a key-value pair to the hash table"""
        index = self.hash(key)
        if self.arr[index] is None:
            self.arr[index] = LinkedList()
        self.arr[index].insert((key, value))


    # helper method for get and contains
    def find_key(self, key):
        index = self.hash(key)
        if self.arr[index] is not None:
            node = self.arr[index].head
            while node:
                if node.value[0] == key:
                    return node
                node = node.next

    def get(self, key):
        """ Returns the value associated with the key """
        if self.find_key(key):
            return self.find_key(key).value[1]

    def contains(self, key):
        """ Returns True if the key is in the hash table """
        return bool(self.find_key(key))


    def keys(self):
        """ Returns all keys in hash table """
        key_list = []
        for e in self.arr:
            if e is not None:
                node = e.head
                while node:
                    key_list.append(node.value[0])
                    node = node.next
        return key_list
