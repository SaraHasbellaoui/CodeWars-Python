# Simple, given a string of words, return the length of the shortest word(s).
str = "bitcoin take over the world maybe who knows perhaps"


def find_short(s):
    l = ""
    l = s.split(" ")
    print(l)
    min = len(l[0])
    print(min)
    for i in range(len(l)):
        if min >= len(l[i]):
            min = len(l[i])
    return min


print(find_short(str))
# An imporved solution:
# def find_short(s):
#     sList = s.split()
#     shortestLength = len(sList[0])
#     for item in sList:
#         if len(item) < shortestLength:
#             shortestLength = len(item)
#     return shortestLength

# Celver solution: using min() function for sorting
#     return min(len(x) for x in s.split())
# Example with map() function
#     return min(map(len, s.split(' ')))
# Example with List Comprehension
#     return min(len(a) for a in s.split())
# Another way:  return len(min(s.split(' '), key=len)). OR
#     s = s.split() # splits the string into a list of individual words
#     l = min(s, key = len) # finds the shortest string in the list
#     return len(l) # returns shortest word length
