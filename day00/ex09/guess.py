from random import randrange
import sys

attempt = 0
lowest = 1
maximum = 99
secret = randrange(lowest, maximum)


def isNb(value):
    try:
        int(value)
        return True
    except Exception:
        return False


def isCorrect(guess):
    if guess == secret:
        return True
    else:
        return False


def main():
    global attempt
    global maximum
    global lowest
    attempt += 1
    guess = input(
        "\nWhat's your guess between {}"
        " and {} ? ".format(lowest, maximum))
    if guess == "exit":
        print("Goodbye!")
        sys.exit()
    if guess == "42":
        print(
            "That's the answer to the ultimate question of life,"
            " the universe and everything!")
    if isNb(guess) is False:
        print("The dumb says {}".format(guess))
        guess = 0
    else:
        guess = int(guess)
        if guess <= lowest or guess >= maximum:
            print("The dumb says {}".format(guess))
            guess = 0
    if guess != 0:
        if isCorrect(guess):
            if attempt == 1:
                print("Congratulations! You got it on your first try!")
            else:
                print("Congratulations, you've got it!")
                print("You won in {} attempts!".format(attempt))
            sys.exit()
        else:
            if guess > secret:
                print("Too high!")
                maximum = guess
            else:
                print("Too low!")
                lowest = guess
    main()


if __name__ == "__main__":
    print(
        "This is an interactive guessing game!\n"
        "You have to enter a number between 1"
        " and 99 to find out the secret number.\n"
        "Type 'exit' to end the game.\n"
        "Good luck!")
    main()
