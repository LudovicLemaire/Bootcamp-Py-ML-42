import sys


def handleError(error):
    print("\x1b[1;31;40mError:\x1b[0m " + error)
    sys.exit()


def printWarning(warning):
    print("\x1b[1;33;40mWarning:\x1b[0m " + warning)


class Vector:
    def __init__(self, args):
        self.values = []
        self.length = 0

        if isinstance(args, list):
            for val in args:
                if isinstance(val, float) is False:
                    handleError("List must be floats.")
            self.values = args
            self.length = len(args)
        elif isinstance(args, tuple):
            if len(args) != 2:
                handleError("Tuple must be filled with 2 integer.")
            for val in args:
                if (isinstance(val, int) is False):
                    handleError("Tuple must be filled with integers.")
            if args[0] == args[1]:
                handleError("Tuple can't have same values.")
            if args[0] < args[1]:
                for i in range(args[0], args[1]):
                    self.values.append(float(i))
            else:
                for i in range(args[1], args[0]):
                    self.values.append(float(i))
            self.length = abs(args[0] - args[1])
        elif isinstance(args, int):
            if args < 1:
                handleError("Integer must be positive.")
            i = 0.0
            for n in range(args):
                self.values.append(i)
                i += 1.0
            self.length = args
        else:
            handleError("Must be a list, tuple or int.")

    def __str__(self):
        return self.__class__.__name__ + str(self.values)

    def __repr__(self):
        self.__str__()

    def __add__(self, vs):
        if isinstance(vs, Vector) and self.length == vs.length:
            for i in range(0, self.length):
                self.values[i] = self.values[i] + vs.values[i]
        elif isinstance(vs, float):
            for i in range(0, self.length):
                self.values[i] = self.values[i] + vs
        else:
            if not isinstance(vs, Vector) and not isinstance(vs, float):
                printWarning("{} is not a Vector nor a float.".format(vs))
            else:
                printWarning(
                    "{} and Vector{} have different length"
                    .format(vs, self.values))
            return
        return self.values

    def __radd__(self, vs):
        return self.__add__(vs)

    def __sub__(self, vs, r=False):
        if isinstance(vs, Vector) and self.length == vs.length:
            for i in range(0, self.length):
                if r is False:
                    self.values[i] = self.values[i] - vs.values[i]
                else:
                    self.values[i] = vs.values[i] - self.values[i]
        elif isinstance(vs, float):
            for i in range(0, self.length):
                if r is False:
                    self.values[i] = self.values[i] - vs
                else:
                    self.values[i] = vs - self.values[i]
        else:
            if not isinstance(vs, Vector) and not isinstance(vs, float):
                printWarning("{} is not a Vector nor a float.".format(vs))
            else:
                printWarning(
                    "{} and Vector{} have different length"
                    .format(vs, self.values))
            return
        return self.values

    def __rsub__(self, vs):
        return self.__sub__(vs, r=True)

    def __truediv__(self, s, r=False):
        if isinstance(s, float):
            for i in range(0, self.length):
                if self.values[i] == 0 or s == 0:
                    printWarning("Division by 0!")
                    return
            for i in range(0, self.length):
                if r is False:
                    self.values[i] = self.values[i] / s
                else:
                    self.values[i] = s / self.values[i]
        else:
            printWarning("{} must be a float.".format(s))
            return
        return self.values

    def __rtruediv__(self, s):
        return self.__truediv__(s, r=True)

    def __mul__(self, vs, r=False):
        if isinstance(vs, Vector) and self.length == vs.length:
            for i in range(0, self.length):
                if r is False:
                    self.values[i] = self.values[i] * vs.values[i]
                else:
                    self.values[i] = vs.values[i] * self.values[i]
        elif isinstance(vs, float):
            for i in range(0, self.length):
                if r is False:
                    self.values[i] = self.values[i] * vs
                else:
                    self.values[i] = vs * self.values[i]
        else:
            if not isinstance(vs, Vector) and not isinstance(vs, float):
                printWarning("{} is not a Vector nor a float.".format(vs))
            else:
                printWarning(
                    "{} and Vector{} have different length"
                    .format(vs, self.values))
            return
        return self.values

    def __rmul__(self, vs):
        return self.__mul__(vs, r=True)
