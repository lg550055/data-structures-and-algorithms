from data_structures.queue import Queue

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree:
    """ Methods to traverse pre, in and post order return a list of values,
        add method adds a node to the tree
        find_maximum_value return the maximum value in the tree
    """

    def __init__(self, root=None, values=None):
        self.root = root
        if values:
            for value in values:
                self.add(value)

    def add(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
            return
        q = Queue()
        q.enqueue(self.root)
        while q:
            front = q.dequeue()
            if not front.left:
                front.left = node
                return
            else:
                q.enqueue(front.left)
            if not front.right:
                front.right = node
                return
            else:
                q.enqueue(front.right)

    def pre_order(self):
        """ root >> left >> right """
        values = []
        def check_nodes(root, values):
            if not root:
                return
            values.append(root.value)
            check_nodes(root.left,values)
            check_nodes(root.right,values)
            return values
        check_nodes(self.root, values)
        return values

    def in_order(self):
        """ left >> root >> right """
        values = []
        def check_nodes(root, values):
            if not root:
                return
            check_nodes(root.left,values)
            values.append(root.value)
            check_nodes(root.right,values)
            return values
        check_nodes(self.root, values)
        return values

    def post_order(self):
        """ left >> right >> root """
        values = []
        def check_nodes(root, values):
            if not root:
                return
            check_nodes(root.left,values)
            check_nodes(root.right,values)
            values.append(root.value)
            return values
        check_nodes(self.root, values)
        return values

    def find_maximum_value(self):
        maxv = self.root.value
        def check_nodes(root):
            nonlocal maxv
            if not root:
                return
            maxv = max(root.value, maxv)
            check_nodes(root.left)
            check_nodes(root.right)
            return maxv
        return check_nodes(self.root)
