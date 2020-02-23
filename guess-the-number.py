import random

def number_game():

    number = random.randint(1,55)
    print("Number range between 1 and 55")

    # print(number)

    guess = int(input("Guess the number: "))

    while guess != number:

        if guess > number:
            print("Nope, Too high")
            guess = int(input("Guess the number: "))
        elif guess < number:
            print("No, too low")
            guess = int(input("Guess the number: "))
        elif guess == number:
            print("Correct!")
        else:
            print("That's not an option")

number_game()

# Stop game from crashing if a str is entered
# Add an option to choose how big the number range is
# Add floating quit or try again menu