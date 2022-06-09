# Breadth-First Traversal of a Graph

## Challenge Summary
Write the following method for the Graph class:

**breadth first:**
- Arguments: Node
- Return: A collection of nodes in the order they were visited.

Display the collection

## Approach & Efficiency

#### Approach
The approach is similar to breadth first traversal for trees.  The key difference is we have to track the vertices visited to avoid revisiting previously visited vertices.  To do this, we use a list of visited vertices.

We enqueue the start node and add it to the visited list.  While there are items on the queue, dequeue (FIFO) vertex and iterate thorugh its neighbors. If neighbor not in visited, then enqueue and append it to visited.

#### Efficiency

The traversal, by looking at all edges, visits each vertex once and adds it to the visited list.  Also, worse-case, the size of the queue may approach the number of vertices.

Time: O(v+e)
Space: O(v+e)

## Solution
To use the breadth_first(vertex) method, import the class Graph from data_structures.graph.  Call the method on a graph with dot notation and pass a vertex in the graph.

## Requirements
Passes all required tests