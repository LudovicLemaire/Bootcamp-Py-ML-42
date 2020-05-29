from NumPyCreator import NumPyCreator
npc = NumPyCreator()

#init colors
red = "\x1b[1;3{};40m".format(1)
green = "\x1b[1;3{};40m".format(2)
yellow = "\x1b[1;3{};40m".format(3)
blue = "\x1b[1;3{};40m".format(4)
purple = "\x1b[1;3{};40m".format(5)
teal = "\x1b[1;3{};40m".format(6)
back = "\x1b[0m"


#from list
print("\n{}{}{}".format(blue, "from_list", back))
entry = [[1,2,3],[6,3,4]]

print("  {purple}entry: {back}{} {yellow}no type{back}".format(entry, purple = purple, yellow = yellow, back = back))
result = npc.from_list(entry)
print("  {teal}result:{back} \n{}\n{teal}  type:{back} {}".format(result, type(result), teal = teal, back = back))

entry = ([7, 8, 10])
print("\n  {purple}entry: {back}{} {yellow}complex{back}".format(entry, purple = purple, yellow = yellow, back = back))
result = npc.from_list(entry, dtype=complex)
print("  {teal}result:{back} \n{}\n{teal}  type:{back} {}".format(result, type(result), teal = teal, back = back))


#from tuple
print("\n{}{}{}".format(blue, "from_tuple", back))
entry = ("a", "b", "c")

print("  {purple}entry: {back}{} {yellow}no type{back}".format(entry, purple = purple, yellow = yellow, back = back))
result = npc.from_tuple(entry)
print("  {teal}result:{back} \n{}\n{teal}  type:{back} {}".format(result, type(result), teal = teal, back = back))

entry = (11, 1, 1010010)
print("\n  {purple}entry: {back}{} {yellow}bytes{back}".format(entry, purple = purple, yellow = yellow, back = back))
result = npc.from_tuple(entry, dtype=bytes)
print("  {teal}result:{back} \n{}\n{teal}  type:{back} {}".format(result, type(result), teal = teal, back = back))


#from iterable
print("\n{}{}{}".format(blue, "from_iterable", back))
entry = range(5)

print("  {purple}entry: {back}{} {yellow}no type{back}".format(entry, purple = purple, yellow = yellow, back = back))
result = npc.from_iterable(entry)
print("  {teal}result:{back} \n{}\n{teal}  type:{back} {}".format(result, type(result), teal = teal, back = back))

print("\n  {purple}entry: {back}{} {yellow}float{back}".format(entry, purple = purple, yellow = yellow, back = back))
result = npc.from_iterable(entry, float)
print("  {teal}result:{back} \n{}\n{teal}  type:{back} {}".format(result, type(result), teal = teal, back = back))


#from shape
print("\n{}{}{}".format(blue, "from_shape", back))
entry = (3, 5)

print("  {purple}entry: {back}{} {yellow}no type{back}".format(entry, purple = purple, yellow = yellow, back = back))
result = npc.from_shape(entry)
print("  {teal}result:{back} \n{}\n{teal}  type:{back} {}".format(result, type(result), teal = teal, back = back))

entry = (6, 2)
print("\n  {purple}entry: {back}{} {yellow}float{back}".format(entry, purple = purple, yellow = yellow, back = back))
result = npc.from_shape(entry, dtype=float)
print("  {teal}result:{back} \n{}\n{teal}  type:{back} {}".format(result, type(result), teal = teal, back = back))


#random
print("\n{}{}{}".format(blue, "random", back))
entry = (3, 2)

print("  {purple}entry: {back}{}".format(entry, purple = purple, yellow = yellow, back = back))
result = npc.random(entry)
print("  {teal}result:{back} \n{}\n{teal}  type:{back} {}".format(result, type(result), teal = teal, back = back))

entry = (4, 3)
print("\n  {purple}entry: {back}{} {yellow}complex{back}".format(entry, purple = purple, yellow = yellow, back = back))
result = npc.random(entry, dtype=complex)
print("  {teal}result:{back} \n{}\n{teal}  type:{back} {}".format(result, type(result), teal = teal, back = back))


#identity
print("\n{}{}{}".format(blue, "identity", back))
entry = 4

print("  {purple}entry: {back}{}".format(entry, purple = purple, yellow = yellow, back = back))
result = npc.identity(entry)
print("  {teal}result:{back} \n{}\n{teal}  type:{back} {}".format(result, type(result), teal = teal, back = back))

entry = 5
print("\n  {purple}entry: {back}{} {yellow}str{back}".format(entry, purple = purple, yellow = yellow, back = back))
result = npc.identity(entry, dtype=str)
print("  {teal}result:{back} \n{}\n{teal}  type:{back} {}".format(result, type(result), teal = teal, back = back))