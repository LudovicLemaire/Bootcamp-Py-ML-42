from vector import Vector
c = {
    "black": "\x1b[1;31;40m",
    "r": "\x1b[1;31;40m",
    "g": "\x1b[1;32;40m",
    "y": "\x1b[1;33;40m",
    "b": "\x1b[1;34;40m",
    "p": "\x1b[1;35;40m",
    "t": "\x1b[1;36;40m",
    "w": "\x1b[1;37;40m",
    "r": "\x1b[0m",
}

def printVS(name, vs):
    print("\x1b[1;34;40m{}:{c} {}\x1b[0m".format(name, str(vs), c = c['r'] if vs is not None else c['y']))


v1 = Vector([0.0, 1.0, 2.0, 3.0])
v2 = Vector(3)
v3 = Vector((10, 15))
v4 = Vector(5)
v5 = Vector([5.0])

print(str(v1))
print(str(v2))
print(str(v3))
print(str(v4))
print(str(v5))

print("\n" + c['t'] + "Add" + c['r'])
printVS(1, str(v1 + v2))
printVS(2, str(v3 + v4))
printVS(3, str(v5 + 4))
printVS(4, str(7.5 + v5))

#re_init Vectors
v1 = Vector([0.0, 1.0, 2.0, 3.0])
v2 = Vector(3)
v3 = Vector((10, 15))
v4 = Vector(5)
v5 = Vector([5.0])

print("\n\x1b[1;36;40mSub\x1b[0m")
printVS(1, str(v1 - v2))
printVS(2, str(v3 - v4))
printVS(3, str(v5 - 4))
printVS(4, str(7.5 - v5))
printVS(5, str(v5 - 5.0))

#re_init Vectors
v1 = Vector([0.0, 1.0, 2.0, 3.0])
v2 = Vector(3)
v3 = Vector((10, 15))
v4 = Vector(5)
v5 = Vector([5.0])

print("\n\x1b[1;36;40mDiv\x1b[0m")
printVS(1, str(v1 / v2))
printVS(2, str(v3 / v4))
printVS(3, str(v5 / 4))
printVS(4, str(7.5 / v5))
printVS(5, str(v5 / 5.0))
printVS(0, str(1.0 / Vector([0.0])))

#re_init Vectors
v1 = Vector([0.0, 1.0, 2.0, 3.0])
v2 = Vector(3)
v3 = Vector((10, 15))
v4 = Vector(5)
v5 = Vector([5.0])

print("\n\x1b[1;36;40mMult\x1b[0m")
printVS(1, str(v1 * v2))
printVS(2, str(v3 * v4))
printVS(3, str(v5 * 4))
printVS(4, str(7.5 * v5))
printVS(5, str(v5 * 5.0))
