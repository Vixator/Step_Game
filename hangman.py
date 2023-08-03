import random

words = ["Pneumonoultramicroscopicsilicovolcanoconiosis ", "Pseudopseudohypoparathyroidism", "Floccinaucinihilipilification", "Honorificabilitudinitatibus", "Thyroparathyroidectomized ", " Antiestablishmentarian ", "Incomprehensibilities", " Sesquipedalianism", "Supercalifragilisticexpialidocious"]

word_to_guess = random.choice(words)
guessed_letters = set()
max_attempts = 8

while max_attempts > 0:
    display = "".join(letter if letter in guessed_letters else "_" for letter in word_to_guess)
    print(display)

    if display == word_to_guess:
        print("Congratulations, You guessed the word:", word_to_guess)
        break

    if guessed_letters:
        print(" letters guessed so far:", " ".join((guessed_letters)))

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
    elif guess in guessed_letters:
        print("You already guessed that letter.")
    else:
        guessed_letters.add(guess)

        if guess not in word_to_guess:
            max_attempts -= 1
            print(f"Wrong guess. Attempts left: {max_attempts}")

if max_attempts == 0:
    print("Game over. The word was:", word_to_guess)
