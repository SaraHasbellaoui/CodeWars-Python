
L1 = [
    {"name": "Bart"},
    {"name": "Lisa"},
    {"name": "Maggie"},
    {"name": "Homer"},
    {"name": "Marge"},
]
L2 = [{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]
L3 = [{'name': 'Bart'},{'name': 'Lisa'}]
L4 = [{'name': 'Bart'}]
L5 = []


s = []
def namelist(list_):
    names = list(map(lambda el: el["name"], list_))

    if len(list_) == 0:
        return ''

    if len(list_) == 1:
        return str(names[0])

    if len(list_) == 2:
        n = " & ".join(el for el in names)
        s.append(n)
        res = ", ".join(el for el in s)
        s.clear()
        return res

    else:
        s.append(names[0])
        return namelist(list_[1 : len(list_)])

# Tests
print(namelist(L1))
print(namelist(L2))
print(namelist(L3))
print(namelist(L4))
print(namelist(L5))

### Alternative Solutions:
# I have solved this challenge using recursion, because there can be an unknown number of elements
# in a list of strings. However, there are many other ways for this challenge to be solved:

# Using negative indices 
def namelist(names):

    names = [ hash["name"] for hash in names ]
    output = names[:-2]
    output.append(" & ".join(names[-2:]))
    return ", ".join(output)

# Using rsplit()
    # compact with a lamda function
namelist=lambda a:' & '.join(', '.join(d['name']for d in a).rsplit(', ',1))
    # not compact
def namelist(names):
    nameList = [elem['name'] for elem in names]
    return ' & '.join(', '.join(nameList).rsplit(', ', 1))

# using format()
def namelist(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), 
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''

# Using replace()
def namelist(names):
  return ", ".join([name["name"] for name in names])[::-1].replace(",", "& ",1)[::-1]


### Notes:
# Slice (start & end index) & Stride (step)
# The syntax is string[start:end:step]

# # Examples
# "123456"[::-2]
# Produces "642" because it'll start from the last character. 
# This is because you didn't provide from which position the slice would be executed. 
# So it'll go back by 2 characters from the last one until it reaches the first one.

# "123456"[1::-2]
# Produces "2" because you told Python to start from the 2nd character (index 1 from the string) and you told Python to go back 2 steps from that position. 
# Which in this case, Python would obviously return just "2". 
# This is because when Python tried to go back by 2 steps, it already hit the first character in the string with just one step.

# "123456"[2::-2]
# So, you told Python to start from the third character (or index 2) and then go back 2 steps from there until it reaches the first character. 
# So it'll start from "3" and then go back 2 steps, and accidentally the first character - which happens to be "1" - has been reached. So Python will give you "31"