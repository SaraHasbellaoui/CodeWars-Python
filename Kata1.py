# Your goal in this kata is to implement a difference function,
# which subtracts one list from another and returns the result.

# Omit repetitions by turing it into a set.
# def array_diff(a, b):
#     a = set(a)
#     b = set(b)
#     a.difference_update(b)
#     a = list(a)
#     return a


# Return the differences without omitting repetitions, as required by tests.
def array_diff(a, b):
    for i in b:  # range(len(b)):
        for x in range(a.count(i)):  # while b[i] in a:
            if a.count(i) != 0:
                # Removes the first item with the specified value
                a.remove(i)
    return a


# Clever solution: List Comprehensions
#  return [element for element in a if element not in b]
# Or, with Lambda Functions: return list(filter(lambda x: x not in b, a))

print(array_diff([1, 1, 2, 3, 4, 4], [1, 3]))
