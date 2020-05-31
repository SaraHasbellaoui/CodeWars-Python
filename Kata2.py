# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.

# 97 to 122; 26 letters
# The pass keyword as name suggests, does nothing.
# It is used as a dummy place holder whenever a syntactical requirement of a certain programming element is to be fulfilled without assigning any operation.

#     pass
#     ord()
#     lower()
#     split()
#     isnumeric()
#     isalpha()

# import re

# def alphabet_position(text):
#     lpos = []
#     # preprocess
#     text = text.lower()
#     text = re.sub(r"[^a-z]", " ", text)
#     print(text)

# # conversion
# for l in text:
#     index = ord(l) - 96
#     if index != -64:
#         lpos.append(str(index))

# spos = " ".join([str(elem) for elem in lpos])
# return spos


import re


def alphabet_position2(text):
    tpos = ""
    # preprocess
    text = text.lower()
    txt = re.findall(r"[a-z]", text)
    print(txt)

    # convert
    tpos = " ".join([str(ord(elem) - 96) for elem in txt])
    return tpos


print(alphabet_position2("Abc def 23g . 'o clock _0"))
print("--------")


def alphabet_position(text):
    spos = ""
    lpos = []
    # preprocess
    text = text.lower()
    text = re.sub(r"[^a-z]", " ", text)
    print(text)

    # convert
    for l in text:
        index = ord(l) - 96
        if index != -64:
            lpos.append(str(index))

    spos = " ".join([str(elem) for elem in lpos])
    return spos


print(alphabet_position("Abc def 23g . 'o clock _0"))

# Clever Solution:
#  return " ".join(str(ord(c)-ord("a")+1) for c in s.lower() if c.isalpha())
#  Another one:  return ' '.join(str(ascii_lowercase.index(n.lower()) + 1) for n in text if n.isalpha())
