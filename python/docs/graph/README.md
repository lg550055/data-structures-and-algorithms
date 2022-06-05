# Graphs
<!-- Short summary or background information -->

## Challenge
Implement a graph represented as an adjacency list with the following methods:
- add node
- get nodes
- size
- add edge
- get neighbors

## Approach & Efficiency

#### Approach
The graph is implemented as an adjacency list.  The adjacency list is a dictionary (hash table).  The keys are the vertices and the values are the edges.  Each edge has a vertex to which it points and a weight (default 0).

#### Efficiency
All operations (add node, get nodes, size, add edge and get neighbors) have an O(1) time complexity. This is because we use a dictionary for the adjacency list.

#### Tests
Functionality tests:
- Node can be successfully added to the graph
- An edge can be successfully added to the graph
- A collection of all nodes can be properly retrieved from the graph
- All appropriate neighbors (edges) can be retrieved from the graph
- Neighbors are returned with the weight between nodes included
- The proper size is returned, representing the number of nodes in the graph
- A graph with only one node and edge can be properly returned
- An empty graph properly returns null

## API
Description of each Graph method:

**add_node**: adds a node to the graph
- Arguments: value
- Returns: the added node

**add_edge**: adds a new edge between two nodes in the graph, if specified, assigns a weight to the edge; default 0. Raises a Key error if either node is not in the graph.
- Arguments: 2 nodes to be connected by the edge, weight
- Returns: nothing

**get_nodes**:
- Arguments: none
- Returns: all of the nodes in the graph as a collection

**get_neighbors**:
- Arguments: node
- Returns: a collection of edges connected to the given node, including the weight of the connection

**size**:
- Arguments: none
- Returns: the total number of nodes in the graph
