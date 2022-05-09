class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree:
    """ Methods to traverse pre, in and post order return a list of values """

    def __init__(self):
        self.root = None

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
