a = "deffe"
b = "cba"
c = set(a).union(set(b))
print(c)
l = list(c)
print(l)
# list.sort sorts the list in place, i.e. it doesn't return a new list.
l.sort()
print(l)


def longest0(a, b):
    s = ""
    l = list(set(a).union(set(b)))
    l.sort()
    for i in l:
        if i.isalpha():
            s += i
    return s

    # s.join(str(i) for i in l if i.isalpha()) this return them separated, implicit join


print(longest0(a, b))

Clever solution:
    return "".join(sorted(set(a1 + a2)))
