import sys
import re
import string


def isNb(value):
    try:
        int(value)
        return True
    except Exception:
        return False


def main(argv):
    if len(argv) != 2:
        print("Wrong number of arguments, 2 are expected")
        sys.exit()
    if re.search('[a-zA-Z]', argv[0]) is None:
        print("First argument must contain a letter")
        sys.exit()
    if isNb(argv[1]) is False:
        print("Second argument must be a number")
        sys.exit()
    else:
        length = int(argv[1])

    sentence = ""
    for letter in argv[0]:
        if (letter in string.punctuation) is False:
            sentence += letter
    words = sentence.split()
    result = []
    for word in words:
        if len(word) > length:
            result.append(word)

    print(result)


if __name__ == "__main__":
    main(sys.argv[1:])
