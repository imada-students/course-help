import sys
import random

def nameGuesser():
	print("Hello, friend. Let's play a nice game, just you and I.")
	print("First, I will think of a number. It will be your job to guess it.")
	print("I'll let you know if you're too high or too low.")
	print("Since I'm so nice, I'll let you pick the upper bound for the number.")
	print("Go right ahead. Input the maximum number you want to guess at.")
	try:
		top = int(sys.stdin.readline())
	except ValueError:
		print("That's not a number, you fool!")
	else:
		if top < 0:
			print("The number should be positive, just because I say so.")
		else:
			num = random.randint(0,top)
			numGuesses = 1
			print("Alright! Everything is in order. I'm now thinking of a number. Try to guess it!")
			guess = readNum("Very funny. Your guess has to be a number too")
			while guess != num:
				if guess < num:
					numGuesses += 1
					print("Too low!")
				elif guess > num:
					numGuesses += 1
					print("Too high!")
				guess = readNum("If you're not gonna play nice, don't play at all.")
			print("Well done! You guessed it!")
			if numGuesses == 1:
				print("Just a single try, damn. Did you cheat?")
			else:
				print("Hm. {} tries. You can do better, probably.".format(numGuesses))


def readNum(msg):
	try:
		guess = int(sys.stdin.readline())
	except ValueError:
		print(msg)
	return guess


nameGuesser()
