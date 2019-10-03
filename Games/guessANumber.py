import random
name = input("Hello! What is your name? ")
val = input(name+"! Guess a number between 1 and 100 ")
num = random.randint(1,101)
if val == num:
    print("Congratulations, you guessed the number!")
else:
    print("You guessed wrong. The number was "+str(num))

