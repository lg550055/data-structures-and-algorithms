class Node:
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left

class BinaryTree:
    """ Has methods to traverse pre, in and post order """

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
