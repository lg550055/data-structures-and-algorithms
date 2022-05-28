# Hash tables
Hash table implementation with set, get, contains, keys and hash methods.

## Challenge Summary
Implement a Hashtable Class with the following methods:

**set**
Hash the key, and set the key and value pair in the table, handling collisions as needed.
Should a given key already exist, replace its value from the value argument given to this method.
- Arguments: key, value
- Returns: nothing

**get**
- Arguments: key
- Returns: Value associated with that key in the table

**contains**
- Arguments: key
- Returns: Boolean, indicating if the key exists in the table already.

**keys**
- Returns: Collection of keys

**hash**
- Arguments: key
- Returns: Index in the collection for that key

## Approach & Efficiency
- **hash** -simple math operation
- All other methods leverage the LinkedList class
- **get** and **contains** -use a helper method to find the subject key.  The helper method iterates through the bucket.
- **set** -adds a key-value pair to the apropriate bucket.
- **keys** -traverses all non-empty buckets.

#### Efficiency
The hash, set, get and contains methods have O(1) time (and space) complexity; unless an extraordinary number of collisions occur.

The keys method has O(n) time complexity.

## Solution
Passes all required and custom tests:

- Successfully hashes a key to an in-range value
- Set a key/value results in the value being in the hash table
- Get a key returns the value stored
- Returns None for a key absent from the hashtable
- Returns a list of all unique keys in the hashtable
- Successfully handles collisions within the hashtable
- Retrieves a value from a bucket that has a collision
