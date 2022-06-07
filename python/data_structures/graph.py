import queue


class Graph:
    """ Implements a graph """
    def __init__(self):
        self._adjacency_list = {}  # leading underscore means internal use only

    def add_node(self, value):
        """ Returns the added vertex """
        vertex = Vertex(value)
        self._adjacency_list[vertex] = []
        return vertex

    def size(self):
        return len(self._adjacency_list)

    def get_nodes(self):
        return self._adjacency_list # use .keys() ?
    
    def add_edge(self, vertex1, vertex2, weight=0):
        if vertex1 not in self._adjacency_list or vertex2 not in self._adjacency_list:
            raise KeyError()
        edge = Edge(vertex2, weight)
        self._adjacency_list[vertex1].append(edge)

    def get_neighbors(self, vertex):
        """ Returns the list of edges of the vertex """
        return self._adjacency_list[vertex]
    
    def breadth_first(self, vertex):
        """ Returns a collection of vertices """
        visited = []
        q = []

        q.append(vertex)
        visited.append(vertex)

        while q:
            vertex = q.pop(0)
            edges = self.get_neighbors(vertex)
            neighbors = [e.vertex for e in edges]
            for v in neighbors:
                if v not in visited:
                    q.append(v)
                    visited.append(v)
        return visited

class Vertex:
    """ Creates a graph vertex """
    def __init__(self, value):
        self.value = value

class Edge:
    """ Creates an edge """
    def __init__(self, vertex, weight):
        self.vertex = vertex # vertex to which the edge points
        self.weight = weight