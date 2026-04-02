secret_number = 23
guess = 0

while guess != secret_number:
    guess = int(input ("Guess the number or be obliterated. "))
    if guess < secret_number:
        print(