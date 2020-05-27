def what_are_the_vars(*args, **kwargs):
    result = []
    dup = []
    for k, v in kwargs.items():
        result.append([k, v])
        dup.append(k)
    for i, v in enumerate(args):
        result.append(["var_{}".format(i), v])
        dup.append("var_{}".format(i))

    if not (len(set(dup)) == len(dup)):
        return None
    else:
        obj = ObjectC()
        for e in result:
            setattr(obj, e[0], e[1])
    return obj


class ObjectC(object):
    def __init__(self):
        pass


def doom_printer(obj):
    if obj is None:
        print("\x1b[1;31;40mERROR\x1b[0m")
        print("\x1b[1;33;40mend\x1b[0m")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("\x1b[1;34;40m{}:\x1b[0m {}".format(attr, value))
    print("\x1b[1;33;40mend\x1b[0m")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
