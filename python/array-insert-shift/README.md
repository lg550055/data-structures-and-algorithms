# Insert to Middle of an Array

## Problem statement

Write a function called insertShiftArray which takes in an array and a value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

**NOTE**: This challenge is whiteboard only.

## Whiteboard
![Whiteboard solution](./array-insert-shift.png)

## Approach & Efficiency
In the interest of maximizing efficiency, this algorithm attempts to conduct the task in a fixed number of steps.  It joins two subsections of the array with an array of the element to insert.  Explicitly, it joins a subarray from the beginning of the array to the middle index to the element array to the subarray from the middle index to the end of the array.

Bottom line: O(1) time and O(N) space

---