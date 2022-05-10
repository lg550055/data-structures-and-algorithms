from data_structures.queue import Queue


def breadth_first(tree):
    output = []
    if tree == None or tree.root == None:
        return output
    queue = Queue()
    queue.enqueue(tree.root)
    while not queue.is_empty():
        current = queue.dequeue()
        output.append(current.value)
        if current.left:
            queue.enqueue(current.left)
        if current.right:
            queue.enqueue(current.right)

    return output
