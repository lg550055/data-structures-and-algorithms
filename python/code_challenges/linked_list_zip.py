from data_structures.linked_list import LinkedList

def zip_lists(a, b):
    zip_list = LinkedList()
    curra = a.head
    currb = b.head
    while curra or currb:
        if curra:
            zip_list.append(curra.value)
            curra = curra.next
        if currb:
            zip_list.append(currb.value)
            currb = currb.next
    return zip_list
