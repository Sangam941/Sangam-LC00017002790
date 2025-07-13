# Rock, Paper, Scisors game terminal based
import random
i = 0
your_count = 0
computer_count = 0

while i<3:
    your_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    if your_choice == computer_choice:
        print("It's a tie!")
    elif (your_choice == "rock" and computer_choice == "scissors") or (your_choice == "paper" and computer_choice == "rock") or (your_choice == "scissors" and computer_choice == "paper"):
        print("You win this round!")
        your_count += 1
    else:
        print("Computer wins this round!")
        computer_count += 1

    i += 1

if(your_count > computer_count):
    print("Congratulations! You won the game!")
elif(your_count < computer_count):
    print("Sorry, you lost the game.")
else:
    print("It's a tie game!")