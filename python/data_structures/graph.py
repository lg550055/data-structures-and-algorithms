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
        return self._adjacency_list # use .keys()?
    
    def add_edge(self, vertex1, vertex2, weight=0):
        if vertex1 not in self._adjacency_list or vertex2 not in self._adjacency_list:
            raise KeyError()
        edge = Edge(vertex2, weight)
        self._adjacency_list[vertex1].append(edge)

    def get_neighbors(self, vertex):
        """ Returns the list of edges of the vertex """
        return self._adjacency_list[vertex]

class Vertex:
    """ Creates a graph vertex """
    def __init__(self, value):
        self.value = value
        self.neighbors = []

class Edge:
    """ Creates an edge """
    def __init__(self, vertex, weight):
        self.vertex = vertex # vertex to which the edge points
        self.weight = weight