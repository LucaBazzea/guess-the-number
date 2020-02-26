import random

def end_menu():

    play_again = " "

    while play_again != "y" and play_again != "n":
        play_again = input("Would you like to play again? [y/n]: ")

        if play_again == "y":
            game()
        else:
            quit

def game():

    number = random.randint(1,30)
    print("Number range between 1 and 30")
    print("---")
    # print(number)

    tries = 0

    while tries < 6:

        while True:
            try:
                guess = int(input("Guess the number: "))
                break
            except:
                print("Input only accepts decimal numbers")
                print("---")

        tries += 1
        if guess > number:
            print("Nope, Too high")
            print("---")
        elif guess < number:
            print("No, too low")
            print("---")
        elif guess == number:
            break

    if guess == number:
        print("Correct!")
    elif guess != number:
        print(f"Wrong, the number was {number}")
    
    end_menu()

game()

# Add an option to choose how big the number range is
# Add a quit or try again menu