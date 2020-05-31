# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.
#
#


def is_isogram(string):
    s_string = set(string.lower())
    if len(string) - len(s_string) == 0:
        return True
    else:
        return False


# Clever Solution:
# return len(string) == len(set(string.lower()))

# Less Clever, creative use of 'count'
#  for letter in string:
#         if string.count(letter) > 1: return False
#     return True

# Another way of detecting duplicates is by testing the key in a dictionary; if it's > 1,
# then it's a duplicate entry
