from data_structures.hashtable import Hashtable


def tree_intersection(t1, t2):
    v1 = t1.in_order()
    v2 = t2.in_order()
    htable = Hashtable()
    for v in v1:
        if v in v2:
            htable.set(v, v)
    return htable.keys()
