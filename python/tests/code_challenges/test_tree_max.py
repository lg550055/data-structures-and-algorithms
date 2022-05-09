import pytest
from data_structures.binary_tree import BinaryTree, Node


# @pytest.mark.skip("TODO")
def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)
    actual = tree.find_maximum_value()
    expected = 30
    assert actual == expected


def test_negs():
    tree = BinaryTree()
    tree.root = Node(-9)
    tree.root.left = Node(-8)
    tree.root.right = Node(-7)
    tree.root.right.left = Node(-5)
    tree.root.right.right = Node(-3)
    actual = tree.find_maximum_value()
    expected = -3
    assert actual == expected
