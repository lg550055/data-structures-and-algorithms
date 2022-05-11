# K-ary tree fizz buzz

## Problem statement

Write a function called fizz buzz tree
- Arguments: k-ary tree
- Return: new k-ary tree

Determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but If the value is divisible:

- 3, replace the value with “Fizz”
- 5, replace the value with “Buzz”
- 3 and 5, replace the value with “FizzBuzz”
- neither 3 nor 5, turn the number into a String

## Whiteboard
![Whiteboard solution](bfs.png)

## Approach & Efficiency
#### Approach
- Use a queue to store the nodes to visit.
- Begin with an empty output list.
- Add the root to the queue
- While there are elements in the queue:
  - Dequeue the front element
  - add each of its left and right nodes to the queue
  - append its value to the output list
- Return the output list.

#### Efficiency: O(N) time and O(n) space

Has to visit every node and create a list with 'n' elements.

## Solution
The approach passes all tests:
- tree = None
- toot = None
- single node tree
- two-node tree
- four-node tree
- four-level tree with child gaps

---

[Back to table of contents](../../README.md)
