# Challenge Summary

- **Create a Node class** that has properties for the value stored in the node, the left child node, and the right child node.

- **Create a Binary Tree class**
  - Define a method for each of the depth first traversals, each of which **returns** an array of the values, ordered appropriately:
    - pre order
    - in order
    - post order
  - Any exceptions or errors that come from your code should be semantic, capture-able errors. Instead of a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong.

- **Create a Binary Search Tree class**
  This class should be a sub-class of the Binary Tree Class, with the following additional methods:
  - Add:
    - **Arguments**: value
    - **Return**: nothing
    - Adds a new node with that value in the correct location in the binary search tree
  - Contains:
    - **Arguments**: value
    - **Return**: boolean indicating whether or not the value is in the tree

## Whiteboard Process
<!-- Embedded whiteboard image -->

## Approach & Efficiency
- Insert: simply assigns a new node to the head and passes the original head as the next to to the new.
  - Time: O(1)
  - Space: O(1)
- Includes: traverses through the list until it finds the target value, in which case it breaks and returns True.  Otherwise, return False
  - Time: O(n)
  - Space: O(1)
- String: traverses through the list adding each value to a string to be formated and returned at the end.
  - Time: O(n)
  - Space: O(n)

## Solution

Can successfully:
- instantiate an empty tree
- instantiate a tree with a single root node
- add a left child and right child properly to a Binary Search Tree
- return a collection from a preorder traversal
- return a collection from an inorder traversal
- return a collection from a postorder traversal
- return true or false for the contains method, given an existing or non-existing node value
