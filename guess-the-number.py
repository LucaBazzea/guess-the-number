import random

number = random.randint(1,30)
print("Number range between 1 and 30")
# print(number)

tries = 0

while tries < 5:

    guess = input("Guess the number: ")
    guess = int(guess)

    tries += 1
    if guess > number:
        print("Nope, Too high")
    elif guess < number:
        print("No, too low")
    elif guess == number:
        break

if guess == number:
    print("Correct!")
elif guess != number:
    print(f"Wrong, the number was {number}")

# Stop game from crashing if a str is entered
# Add an option to choose how big the number range is
# Add floating quit or try again menu