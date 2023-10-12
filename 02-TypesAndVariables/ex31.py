import random
dice = random.randint(1,6)
guess = input("Enter your guess: ")
check = dice == guess
print(f"Challenge won: {check}")