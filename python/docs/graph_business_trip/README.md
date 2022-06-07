# Graph Business Trip

## Challenge Summary
Write a function called business trip
- Arguments: graph, array of city names
- Return: the cost of the trip (if it’s possible) or null (if not)

## Approach & Efficiency

#### Approach

Use a helper function to calculate the cost of a trip between a pair of locations.  Returns the cost if the locations are connected, or False otherwise.

Since a trip may involve more than one location, iterate through the list of locations forming pairs in each iteration.  Then call the cost helper function.  If it returns False, then return False, 0.  Otherwise, add the cost to the cost accumulator.  Once all pairs have been evaluated, return True, cost accumulator.

#### Efficiency

Time: O(n)
Space: O(n)

## Requirements

Passes all required and custom tests
