# Depth First Traversal

## Challenge
Write a Depth first method for the Graph class:
- Arguments: Node (Starting point of search)
- Return: A collection of nodes in their pre-order depth-first traversal order
- Program output: Display the collection

## Approach & Efficiency

#### Approach

Just like in tree traversal, the approach to depth first in graphs uses recursion.  Similarly to breadth first, depth first uses a list of visited vertices to ensure each vertex is only visited once.

#### Efficiency

The traversal, by looking at all edges, visits each vertex once and adds it to the visited list.  Also, worse-case, the call stack may approach the number of vertices.

Time: O(v+e)
Space: O(v+e)

## Requirements: passes all tests

Tests passes:

- Empty graph / root not in graph
- Single vertex
- Two vertices
- Two vertices, two edges
- Multiple vertices and multiple edges
