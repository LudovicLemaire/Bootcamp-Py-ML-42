import sys


def isNb(value):
    try:
        int(value)
        return True
    except Exception:
        return False


isError = False
if len(sys.argv) != 2:
    isError = True
elif isNb(sys.argv[1]) is False:
    isError = True

if isError:
    print("ERROR")
    sys.exit()

nb = int(sys.argv[1])

if nb == 0:
    print("I'm Zero.")
elif nb % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
