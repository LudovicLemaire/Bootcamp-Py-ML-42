import random
import datetime


def strSort(word):
    return word.lower()


def rnDup(words):
    seen = set()
    seen_add = seen.add
    return [x for x in words if not (x in seen or seen_add(x))]


def generator(txt, sep=" ", option=None):
    """Option is an optional arg, sep is mandatory"""
    if not isinstance(txt, str):
        yield 'ERROR'
        return 'ERROR'
    if option and option not in ['shuffle', 'unique', 'ordered']:
        yield 'ERROR'
        return 'ERROR'
    if option == 'shuffle':
        txtList = txt.split(sep=sep)
        rNb = str(
            int(datetime.datetime.now().strftime('%f'))
            ** int(len(txtList) / 2))
        result = []
        for i, v in enumerate(txtList):
            result.insert(int(rNb[i]), v)
        for e in result:
            yield e
        pass
    elif option == 'unique':
        for e in rnDup(txt.split(sep=sep)):
            yield e
    elif option == 'ordered':
        for e in sorted(txt.split(sep=sep), key=strSort):
            yield e
    elif option is None:
        for e in txt.split(sep=sep):
            yield e
