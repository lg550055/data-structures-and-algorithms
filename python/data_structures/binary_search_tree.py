from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """ Adds a node (other than duplicate).  Returns True if tree contains value """

    def add(self, value):
        """ Adds node to BST """
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        
        def check_nodes(node):
            if not node:
                return
            if value < node.value:
                if node.left:
                    check_nodes(node.left)
                else:
                    node.left = new_node
            else:
                if node.right:
                    check_nodes(node.right)
                else:
                    node.right = new_node

        check_nodes(self.root)


    def contains(self, value):
        """ Returns True if value in BST """
        def check_nodes(node):
            if node:
                if node.value == value:
                    return True
                elif node.value > value:
                    return check_nodes(node.left)
                else:
                    return check_nodes(node.right)
            else:
                return False

        return check_nodes(self.root)
