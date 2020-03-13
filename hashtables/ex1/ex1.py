"""
# Merging Two Packages

Given a package with a weight limit `limit` and a list `weights` of item weights, implement a function `get_indices_of_item_weights` that finds two items whose sum of weights equals the weight limit `limit`. Your function will return an instance of an `Answer` tuple that has the following form:
```
(zero, one)
```
where each element represents the item weights of the two packages. _**The higher valued index should be placed in the `zeroth` index and the smaller index should be placed in the `first` index.**_ If such a pair doesn’t exist for the given inputs, your function should return `None`.

_NOTE:_ When calling `hash_table_retrieve` with a key that doesn't exist in the hash table, `hash_table_retrieve` will return `None`. 

Your solution should run in linear time.

Example:
```
input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
```

## Hints
 
* A brute-force solution would involve two nested loops, yielding a quadratic-runtime solution. How can we use a hash table in order to implement a solution with a better runtime?
* Think about what we can store in the hash table in order to help us to solve this problem more efficiently. 
* What if we store each weight in the input list as keys? What would be a useful thing to store as the value for each key? 
* If we store each weight's list index as its value, we can then check to see if the hash table contains an entry for `limit - weight`. If it does, then we've found the two items whose weights sum up to the `limit`!
"""

#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

# This almost works :/
# def get_indices_of_item_weights(weights, length, limit):

#     """
#     YOUR CODE HERE
#     """
#     ht = HashTable(16)

#     for i in range(length):
#         target = limit - weights[i]
#         current_value = weights[i]



#         if hash_table_retrieve(ht, target) is not None:
#             hash_table_insert(ht, current_value, i)
#             answer = (hash_table_retrieve(ht, current_value), hash_table_retrieve(ht, target))
#             print(answer)
#             return answer
#         else:
#             hash_table_insert(ht, current_value, i)

#     return None


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    for i in range(length):
        current_value = weights[i]
        hash_table_insert(ht, current_value, i)

    for i in range(length):
        target = limit - weights[i]
        answer = hash_table_retrieve(ht, target)

        if answer is not None:
            return (answer, i)

    return None


# def get_indices_of_item_weights(weights, length, limit):

#     """
#     YOUR CODE HERE
#     """
#     ht = {}
#     count = 0

#     for i in range(length):
#         target = limit - weights[i]
#         current_value = weights[i]



#         if target in ht:
#             ht[current_value] =  i
#             answer = (ht[current_value], ht[target])
#             return answer
#         else:
#             ht[current_value] =  i
#             print(ht)

#     return None

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

weights = [ 4, 6, 10, 15, 16 ] 
length = 5
limit = 21

print(get_indices_of_item_weights(weights, length, limit))