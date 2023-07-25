import random

def get_range_from_user():
    while True:
        try:
            name=input("What is your name: ")
            min_range = 1
            max_range = int(input("Enter the maximum range number: "))
            if min_range >= max_range:
                print("Invalid range. Please ensure the minimum range is less than the maximum range.")
            else:
                return min_range, max_range
        except ValueError:
            print("Invalid input. Please enter valid integer numbers.")

def generate_random_number(min_range, max_range):
    return random.randint(min_range, max_range)

def get_player_guess():
    while True:
        try:
            guess = int(input("Make a guess: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a valid integer number.")

def play_guess_the_number_game():
    min_range, max_range = get_range_from_user()
    target_number = generate_random_number(min_range, max_range)
    print(f"I have picked a number between {min_range} and {max_range}.")
    attempts = 0
    while True:
        attempts += 1
        player_guess = get_player_guess()
        
        if player_guess == target_number:
            print(f"You guessed the correct number {target_number} in {attempts} attempts.")
            break
        elif player_guess < target_number:
            print("The number is higher than your guess.")
        else:
            print("The number is lower than your guess.")

if __name__ == "__main__":
    play_guess_the_number_game()
