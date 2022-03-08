import random 

secretnumber = random.randint(1,20)
print("I am thinking of a number between 1 and 20")

#Ask the player to guess 6 times
for guessesTaken in range(1, 7):
	print("Take a guess")
	guess = int(input())

	if guess < secretnumber:
		print("Your guess is too low")
	elif guess > secretnumber:
		print("Your guess is too high")
	else:
		break

if guess == secretnumber:
	print("Good job! You have guessed the secret number in " + str(guessesTaken) + " guesses")
else:
	print("No, the number was " + str(secretnumber))