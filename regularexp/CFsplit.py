

import re

S = input()


s = re.split(r'(\([a-zA-z_]{1,}\))',S)

print(s)
print(re.findall(r"\([^()]*\)", S))

# a = [word for e in re.split(r"\([^()]*\)",S) for word in re.split(r"_+", e)]
# b = [word for e in re.findall(r"\([^()]*\)", S) for word in re.split(r"_+", e[1:-1]) if word]
# print(str(len(max(a, key=len))) + " " + str(len(b)))
print('(and_Petya)'[1:-1])