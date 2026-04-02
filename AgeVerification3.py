name = input("What is your name knight in training? ")
age = int(input("How old are you? "))
if age <= 13:
    print(f"Ah! {name} you're far to young, start as a squire and work your way up to knighthood.")
elif age <= 17:
    print(f"Ah! {name} you're a teen, you can start your training as a knight but you have to wait until you're 18 to be knighted.")
else:
    print(f"Ah! {name} you're an adult, you can start your training as a knight and be knighted whenever you complete your training.")
