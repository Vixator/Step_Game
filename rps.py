import random

choices = ("rock", "paper", "scissors")

attempts=0

while True:
    choice = input("Pick Rock, Paper, or Scissors: ").lower()
    computerchoice = random.choice(choices)
    
    if choice=="end":
        print(f"You played {attempts} rounds")
        break

    if choice == computerchoice:
        print("It's a tie")
        print(computerchoice)
        attempts+=1
    elif choice == "rock" and computerchoice == "scissors" or \
         choice == "paper" and computerchoice == "rock" or \
         choice == "scissors" and computerchoice == "paper":
        print("You win")
        print(computerchoice)
        attempts+=1
    else:
        print("You lose")
        print(computerchoice)
        attempts+=1
        
