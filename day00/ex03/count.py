import string
import sys


def text_analyzer(*arguments):
    """This function counts the number of words, characters, upper characters\
        , lower characters, punctuation and spaces in a given text."""
    if len(arguments) > 1:
        print("ERROR")
        sys.exit()
    if len(arguments) == 0:
        text = input("What is the text to analyse? ")
        print(text)
    else:
        text = arguments[0]
    words = text.split()
    character = 0
    uppercase = 0
    lowercase = 0
    punctuationMarks = 0
    space = 0

    for letter in text:
        character += 1
        if letter.isupper():
            uppercase += 1
        if letter.islower():
            lowercase += 1
        if letter in string.punctuation:
            punctuationMarks += 1
        if letter == ' ':
            space += 1

    print('The text contains {} words for {} characters:\
        '.format(len(words), character))
    print('- {} upper letters'.format(uppercase))
    print('- {} lower letters'.format(lowercase))
    print('- {} punctuation marks'.format(punctuationMarks))
    print('- {} spaces'.format(space))
