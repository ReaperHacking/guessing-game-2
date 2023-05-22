# Importing Random Module and Introduction!
import random

print("Welcome to the second guessing game on my github!\n")
print("Think of a number in your head, 0-100, and the computer will try to guess it. Tell the computer if it's too high or too low or exactly right!\n")
print("However, if it's way lower or way higher than the number the computer guesses, just type 'way lower' or 'way higher' \n")

# While loop to ask the user if they want to play again
play_again = "Y"
while play_again == "Y":
    # Setting Variables and so that the computer guesses random numbers
    rand_numbers = random.randint(0, 100)
    computer_guess = rand_numbers
    guesses = 0

    # Nested while loop
    while True:
        too_high_or_too_low = input(str(computer_guess) + " ---> ").lower()
        guesses += 1

        if too_high_or_too_low == 'too high':
            computer_guess -= 1
        elif too_high_or_too_low == 'too low':
            computer_guess += 1
        elif too_high_or_too_low == 'way higher':
            computer_guess += 10
        elif too_high_or_too_low == 'way lower':
            computer_guess -= 10
        elif too_high_or_too_low == 'exactly right':
            print(f'It took me {guesses} guesses to guess your number!\n')
            break

        else:
            print("Error, you didn't choose too high, too low, way higher, way lower, or exactly right.")

    # Restart Function asking user if they would like to continue
    restart = input("Would you like to play again? (Y/N): ").upper()
    if restart == 'N':
        print("Ok, thank you for playing!")
        break
