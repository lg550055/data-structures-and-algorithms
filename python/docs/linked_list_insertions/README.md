# Challenge Summary - Linked List Insertions

Write the following methods for the **Linked List class**:
  - **append**:
    - Arguments: new value
    - Returns: nothing
    - Adds a new node with that value to the end of the list.
  - **insert before**:
    - Arguments: value, new value
    - Returns: nothing
    - Adds a new node with the given new value immediately before the first node that has the value specified
  - **insert after**:
    - Arguments: value, new value
    - Returns: nothing
    - Adds a new node with the given new value immediately after the first node that has the value specified

## Whiteboard Process
<!-- Embedded whiteboard image -->

## Approach & Efficiency
- append: traverses to the end of the list and assigns a new node as the next to the original tail node
  - Time: O(n)
  - Space: O(1)
- insert before: traverses through the list until it finds a pointer to the target value.  Then, assigns that pointer to the new node, to which it assigns a pointer to the next value
  - Time: O(n)
  - Space: O(1)
- insert after: traverses through the list until it finds the target value.  Then, assigns its pointer to the new node, to which it assigns a pointer to the next value
  - Time: O(n)
  - Space: O(1)

## Solution
To use these methods, import the LinkedList class, create an instance, then call them with dot notation.

`my_linked_list = LinkedList()`
`my_linked_list.insert('red')`
`my_linked_list.append('blue')`
`my_linked_list.insert_before('blue','white)`