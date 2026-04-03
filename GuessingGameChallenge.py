import random
secret_number = random.randint(1, 100)
guess = 0
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    guess = int(input("Guess the number or be obliterated: "))
    attempts += 1

    print(f"Attempt {attempts} of {max_attempts}")

    if guess < secret_number:
        print("Too low. Try again.")
    elif guess > secret_number:
        print("Too high. Come on.")
    else:
        print("Congratulations! You guessed the number.")
        break
if guess != secret_number:
    print("Game over. You failed.")
