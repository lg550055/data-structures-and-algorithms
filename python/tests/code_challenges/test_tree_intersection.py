import pytest
from code_challenges.tree_intersection import tree_intersection
from data_structures.binary_tree import BinaryTree, Node
from data_structures.queue import Queue


def test_exists():
    assert tree_intersection


def test_small():
    tree_a = BinaryTree()
    values = [1, 5]
    add_values_to_empty_tree(tree_a, values)
    tree_b = BinaryTree()
    values = [4, 5]
    add_values_to_empty_tree(tree_b, values)
    actual = tree_intersection(tree_a, tree_b)
    expected = [5]
    assert sorted(actual) == sorted(expected)


def test_no_common():
    tree_a = BinaryTree()
    values = [1, 5]
    add_values_to_empty_tree(tree_a, values)
    tree_b = BinaryTree()
    values = [4, 2]
    add_values_to_empty_tree(tree_b, values)
    actual = tree_intersection(tree_a, tree_b)
    expected = []
    assert sorted(actual) == sorted(expected)


def test_one_empty():
    tree_a = BinaryTree()
    values = [1, 5]
    add_values_to_empty_tree(tree_a, values)
    tree_b = BinaryTree()
    values = []
    add_values_to_empty_tree(tree_b, values)
    actual = tree_intersection(tree_a, tree_b)
    expected = []
    assert sorted(actual) == sorted(expected)


def test_almost_same():
    tree_a = BinaryTree()
    values = [1, 5, 7, 9]
    add_values_to_empty_tree(tree_a, values)
    tree_b = BinaryTree()
    values = [1, 5, 7, 9, 11]
    add_values_to_empty_tree(tree_b, values)
    actual = tree_intersection(tree_a, tree_b)
    expected = [1, 5, 7, 9]
    assert sorted(actual) == sorted(expected)


# @pytest.mark.skip("TODO")
def test_tree_intersection():
    tree_a = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)
    tree_b = BinaryTree()
    values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
    add_values_to_empty_tree(tree_b, values)
    actual = tree_intersection(tree_a, tree_b)
    expected = [125, 175, 100, 160, 500, 200, 350]
    assert sorted(actual) == sorted(expected)


def add_values_to_empty_tree(tree, values):
    """
    Helper function to add given values to BinaryTree
    """
    if values:
        tree.root = Node(values.pop())
        q = Queue()
        q.enqueue(tree.root)
        while values:
            node = q.dequeue()
            node.left = Node(values.pop())
            node.right = Node(values.pop()) if values else None
            q.enqueue(node.left)
            q.enqueue(node.right)
