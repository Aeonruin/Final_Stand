game = input("What's your favorite game? ")
hours = int(input("How many hours do you put into your game per week? "))
if hours <= 20:
    print(f"You play {game} a lot, but not too much. pretty casual.")
elif hours <= 50:
    print(f"You have some balance in you life, playing {game} hasn't consumed your life.")
else:
    print(f"You play {game} quite a lot. almost too much. you're hardcore.")