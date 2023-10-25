import mymath
import mykeyboard

user_guess = mykeyboard.read_number()
computer = mymath.generate_number()

if user_guess == computer:
    print(f"Entered number: {user_guess}")
    print(f"Computer number: {computer}")
    print("You won the game!")
else:
    print(f"Entered number: {user_guess}")
    print(f"Computer number: {computer}")
    print("You lost the game!")