import re
Str = "This website is for losers LOL!"


def disemvowel(strin):
    strin = re.sub(r"[aeiou]", "", strin, flags=re.IGNORECASE)
    return strin


print(disemvowel(Str))

print("Ths wbst s fr lsrs LL!")


# Refactored:
# def disemvowel(string):
#     return re.sub(r'[aeiou]', '', string, flags=re.IGNORECASE)

# Other solutions:
#  return s.translate(None, "aeiouAEIOU") // With translate method
#  return "".join(c for c in string if c.lower() not in "aeiou") // With a List Comprehension
# PS: this is a valid if statement in Python:  if not str2handle[i] in vowel_character:
