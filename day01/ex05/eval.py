def printWarning(warning):
    print("\x1b[1;33;40mWarning:\x1b[0m " + warning)


def hasError(coefs, words):
    if isinstance(coefs, list) is False or isinstance(words, list) is False:
        printWarning("coefs and words must be arrays.")
        return True
    if len(coefs) != len(words):
        printWarning(
            "coefs and words must be same length [{}, {}]."
            .format(len(coefs), len(words)))
        return True
    for i, v in enumerate(coefs):
        if isinstance(coefs[i], float) is False:
            printWarning("coefs must be an array of float.")
            return True
        if isinstance(words[i], str) is False:
            printWarning("words must be an array of string.")
            return True
    return False


class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if hasError(coefs, words) is True:
            return -1
        print(sum([e[0] * len(e[1]) for e in zip(coefs, words)]))
        return 1

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if hasError(coefs, words) is True:
            return -1
        print(sum([coefs[i] * len(words[i]) for i, v in enumerate(coefs)]))
        return 1
