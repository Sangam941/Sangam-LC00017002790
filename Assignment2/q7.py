# 7. Create a loop that keeps asking the user to guess a secret number between 1 to 10 until they guess it correctly. (Use while loop and break)

import math
from random import randint

i = 0
number = math.ceil(randint(1, 10))  # Random secret number between 1 and 10

while True:
    guess = int(input("Guess the secret number between 1 and 10: "))
    if guess == number:  
        print("Congratulations! You've guessed the secret number.")
        break
    else:
        print("Wrong guess, try again.")
    i += 1