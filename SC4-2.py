game = input("What game will you be adding into your stock? ")
genre = input("What genre does the game belong to? ")
rating = int(input("What rating would you give the game? "))

print(f"Game: {game}, Genre: {genre}, Rating: {rating}")
print(f"So {game} is a {genre} game with a rating of {rating}? Nice choice!")
if rating >= 7:
    print(f"{game} is a great game! You should definitely play it.")
else:    print(f"{game} is not a great game. You might want to reconsider adding it to your stock.")   