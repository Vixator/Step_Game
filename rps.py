import random
while True:
 userscore=0
 computerscore=0
 userinput=input("Pick a action (rock, paper, scissors) ")
 actions=["rock", "paper", "scissors"]
 computerinput=random.choice(actions)
 print(f"\nYou chose {userinput}, computer chose {computerinput}.\n")
 if (userinput)==(computerinput):
 print(f"\nYou chose {userinput}, computer chose {computerinput} is it a tie?\n")
 elif (userinput) == "rock":
 if (computerinput) == "scissors":
 print("Rock beats scissors")
 userscore+=1
 print(f"\nYour score is {userscore}, computer score is {computerscore}\n")
 else:
 print("Paper beats rock")
 computerscore+=1
 print(f"\nYour score is {userscore}, computer score is {computerscore}\n")
 elif (userinput) == "paper":
 if (computerinput) == "rock":
 print("Paper beats rock")
 (userscore)+=1
 print(f"\nYour score is {userscore}, computer score is {computerscore}\n")
 else:
 print("Scissors beats paper")
 (computerscore)+=1
 print(f"\nYour score is {userscore}, computer score is {computerscore}\n")
 elif userinput == "scissors":
 if computerinput == "paper":
 print("Scissors beats paper")
 (userscore)+=1
 print(f"\nYour score is {userscore}, computer score is {computerscore}\n")
 else:
 print("Rock beats scissors")
 (computerscore)+=1
 print(f"\nYour score is {userscore}, computer score is {computerscore}\n")
 continue
 
 
 


