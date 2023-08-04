# This is a simple number guessing game where the user has to guess a randomly generated number by the computer.
# The computer's guess is generated randomly within the specified range,
# and the user has a limited number of attempts to guess the correct number.
# The user should use a binary search algorithm.
# The number of attempts the user needs is limited by maximum_num_guess,
# which is calculated as the ceiling of the base-2 logarithm of the range_number.
import random
import math
import numpy
range_number = int(input("Please provide the range for the game: "))
computer_guess = random.randint(1, range_number)
maximum_num_guess = math.ceil(numpy.log2(range_number))

for i in range(maximum_num_guess):
    user_guess = int(input("Please provide your "+str(i+1)+" guess:"))
    if user_guess == computer_guess:
        print("You WIN!!")
        quit()
    elif user_guess > computer_guess:
        print("Your guess is too big!")
    else:
        print("Your guess is too small!")

print("You lose!\nThe computer guess was:", computer_guess)
