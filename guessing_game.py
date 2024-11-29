import random

print("Hi, welcome to the game. This is a number guessing game.\nREMEMBER, You got 7 chances to guess the number. Let's get start the game")
lower_bound = int(input("Enter Lower bound: "))
higher_bound = int(input("Enter Upper bound: "))
number_to_guess = random.randrange(lower_bound, higher_bound)
chances = 7
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    my_guess = int(input('Please enter your guess: '))

    # When user wins the game
    if my_guess == number_to_guess:
        print(f"The number is {number_to_guess} and you found it right in the {guess_counter} attempt")
        break

    # When user loses the game
    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f"Oops sorry, the number is: {number_to_guess} better luck next time!")
        break

    # When entered number is greather than number to guess
    elif my_guess > number_to_guess:
        print('Your guess is higher. Try again')

    # When entered number is lower than number to guess
    elif my_guess < number_to_guess:
        print('Your guess is lesser. Try again')
