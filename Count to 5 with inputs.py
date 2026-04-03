name = 0

while name < 5:
    int(input("Enter a random number to continue the chain. "))
    name += 1
    print(f"{name} out of 5")
if name == 5:
    print("Congratulations! You have completed the chain.")