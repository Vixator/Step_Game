
import random

words=("abjure","future","picnic","camera","interim","shellfish","campus","invest","ship","cat","fish","jackpot","significance","carsick","kitchenette","sometimes")
word_to_guess = random.choice(words)
guessed_letters = set()
max_attempts = 8

while True:
    display = "".join(letter if letter in guessed_letters else "_" for letter in word_to_guess)
    print(display)

    if display == word_to_guess:
        print("Congratulations, You guessed the word:", word_to_guess)
        break
    guess = input("Guess a letter").lower()
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.add(guess)
    if guess not in word_to_guess:
        max_attempts -= 1
        print(f"Wrong guess. Attempts left: {max_attempts}")
        if max_attempts == 0:
            print("Game over. The word was:", word_to_guess)
            break
