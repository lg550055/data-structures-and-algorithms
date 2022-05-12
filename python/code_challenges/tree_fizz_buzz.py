from data_structures.kary_tree import KaryTree, Node
from data_structures.queue import Queue

def fizz_buzz(value):
    if value % 3 == 0 and value % 5 == 0:
        return 'FizzBuzz'
    elif value % 3 == 0:
        return 'Fizz'
    elif value % 5 == 0:
        return 'Buzz'
    else:
        return str(value)

def fizz_buzz_tree(tree):
    output = KaryTree()
    q = Queue()
    aux = Queue()

    output.root = Node(fizz_buzz(tree.root.value))
    for child in tree.root.children:
        q.enqueue(child)
        aux.enqueue(output.root)

    while not q.is_empty():
        node = q.dequeue()

        target_node = aux.dequeue()
        child_node = Node(fizz_buzz(node.value))
        target_node.children.append(child_node)

        for child in node.children:
            q.enqueue(child)
            aux.enqueue(child_node)

    return output
