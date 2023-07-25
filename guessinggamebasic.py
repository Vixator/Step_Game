import random
attempts=0
name = input("What is your name? ")
minrange = 1  
maxrange = int(input("What is the maximum number of your range? "))
while True:
    try:
        number = random.randint(minrange, maxrange)
        break 
    except ValueError:
        print("Invalid input. Please enter a valid integer number.")

print(f"Hi, {name}! I have picked a number between {minrange} and {maxrange}.")

while True:
    try:
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"Congratulations, {name}! You guessed the correct number {number} in {attempts} guesses.")
            break
        elif guess < number:
            print("The number is higher than your guess.")
            attempts+=1
        else:
            print("The number is lower than your guess.")
            attempts+=1
    except ValueError:
        print("Invalid input. Please enter a valid integer number.")
        attempts+=1
humansecret=input(f"What is your secret number in a range of {minrange} to {maxrange}")

number=humansecret
compattempts=0
low=minrange
high=maxrange
mid=(low+high)/2
while True:
    if number==mid:
        print(f"Computer guessed your number of {humansecret} in {compattempts} attempts")
        compattempts+=1
    elif number>mid:
        low==mid+1
        high==100
        mid==(low+high)/2
        compattempts+=1
    else:
        low==1
        high==mid-1
        mid==(low+high)/2
        attempts+=1
    


