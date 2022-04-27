# Challenge Summary

- **Create a Node class** that has properties for the value stored in the Node, and a pointer to the next Node.
- **Create a Linked List class**
  - Include a head property
  - Upon instantiation, an empty Linked List should be created.
  - Add an **insert method**:
    - Arguments: value
    - Returns: nothing
    - Adds a new node with that value to the head of the list with an O(1) Time performance.
  - Add an **includes method**:
    - Arguments: value
    - Returns: Boolean, which indicates whether that value exists as a Node’s value in the list.
  - Add a to **string method**:
    - Arguments: none
    - Returns: a string representing all the values in the Linked List, formatted as: "[ a ] -> [ b ] -> [ c ] -> NULL"

## Whiteboard Process
<!-- Embedded whiteboard image -->

## Approach & Efficiency
- Insert: simply assigns a new node to the head and passes the original head as the next to to the new.
  - Time: O(1)
  - Space: O(1)
- Includes: traverses through the list until it finds the target value, in which case it breaks and returns True.  Otherwise, return False
  - Time: O(n)
  - Space: O(1)
- String: traverses through the list adding each value to a string to be formated and returned at the end.
  - Time: O(n)
  - Space: O(n)

## Solution
<!-- Show how to run your code, and examples of it in action -->