import sys
morse = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    " ": "/",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----"
}

def main(argv):
    if len(argv) == 0:
        print("Wrong number of arguments, 1 is expected")
        sys.exit()
    sentence = ' '.join(argv).lower()
    for letter in sentence:
        if letter.isalnum() is False and letter != ' ':
            print("Argument must contain alphanumeric characters only")
            sys.exit()
    result = []
    for letter in sentence:
        result.append(morse[letter])
    print(' '.join(result))


if __name__ == "__main__":
    main(sys.argv[1:])
