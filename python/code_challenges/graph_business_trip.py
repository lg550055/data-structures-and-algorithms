from data_structures.graph import Graph, Vertex


def direct_flights(graph, cities):
    """ Returns True, cost if trip is possible, otherwise False, 0 """
    
    def direct(origin, destination):
        for v in graph.get_nodes().keys():
            if v.value == origin:
                edges = graph.get_neighbors(v)
        for e in edges:
            if e.vertex.value == destination:
                return e.weight
        return False

    cost = 0
    for i in range(len(cities)-1):
        origin = cities[i]
        destination = cities[i+1]
        pair = direct(origin, destination)
        if not pair:
            return False, 0
        cost += pair
    return True, cost
