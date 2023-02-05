import random

def create_default_hint(secretStr):
    return ['_'] * len(secretStr)
def format_pluralization(str, num, suffix):
    return f'{str}{"" if num == 1 else suffix}'

secrets_list = ['mosiah', 'temple', 'moroni', 'nephi', 'alma', 'helaman']
secret = random.choice(secrets_list)
guess = ''
hint = create_default_hint(secret)
guess_num = 0
incorrect_length = False

print("Welcome to the word guessing game! The computer will randomly assign the secret word for guessing.\n")

while True:
    try:
        max_attempts = int(input("Set the maximum allowed attempts: "))
    except ValueError:
        print("Please, enter a valid integer.")
        continue
    else:
        break

print("<---------------------------------------------------------------->")

while guess != secret and guess_num < max_attempts:
    if(not incorrect_length):
        print(f"Your hint is: {' '.join(hint)}")
    guess = input("What is your guess? ").lower()
    hint = create_default_hint(secret)
    if(len(guess) != len(secret)):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        print()
        incorrect_length = True
    else: 
        incorrect_length = False
        for index, letter in enumerate(guess):
            if(letter in secret):
                hint[index] = letter.upper() if secret[index] == letter else letter
    guess_num += 1

if(guess == secret):
    print("Congratulations! You guessed it!")
    print(f"It took you {guess_num} {format_pluralization('guess', guess_num, 'es')}.")
elif(guess_num >= max_attempts):
    print("Game over! You have spent all your attempts!")
else:
    print("Game over!")

