# Breadth First Search

## Problem statement

Write a function called breadth first
- Arguments: tree
- Return: list of all values in the tree, in the order they were encountered

## Whiteboard
![Whiteboard solution](bfs.png)

## Approach & Efficiency
#### Approach
- Use a queue to store the nodes to visit.
- Begin with an empty output list.
- Add the root to the queue
- While there are elements in the queue:
  - Dequeue the front element
  - add each of its left and right nodes to the queue
  - append its value to the output list
- Return the output list.

#### Efficiency: O(N) time and O(n) space

Has to visit every node and create a list with 'n' elements.

## Solution
The approach passes all tests:
- tree = None
- toot = None
- single node tree
- two-node tree
- four-node tree
- four-level tree with child gaps

---

[Back to table of contents](../../README.md)
