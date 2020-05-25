import sys


def isNb(value):
    try:
        int(value)
        return True
    except Exception:
        return False


largv = len(sys.argv)
usage = "Usage: python operations.py <number1> <number2>\n\
    Example:\n  python operations.py 10 3"
if largv == 3:
    if False in [isNb(sys.argv[1]), isNb(sys.argv[2])]:
        print("InputError: only numbers\n")
        print(usage)
        sys.exit()
else:
    if largv < 3:
        print(usage)
    else:
        print("InputError: too many arguments\n")
        print(usage)
    sys.exit()

fNb = int(sys.argv[1])
sNb = int(sys.argv[2])
print('Sum:         {}'.format(sum([fNb, sNb])))
print('Difference:  {}'.format(abs(fNb - sNb)))
if 0 in [fNb, sNb]:
    print('Quotient:    {}'.format("ERROR (div by zero)"))
    print('Remainder:   {}'.format("ERROR (modulo by zero)"))
else:
    print('Quotient:    {}'.format(fNb / sNb))
    print('Remainder:   {}'.format(fNb % sNb))
