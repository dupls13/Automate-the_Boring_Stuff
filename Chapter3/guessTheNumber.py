#Number guessing game 
import random 

secretnumber= random.randint(1,100)
print("I am thinking of a number between 1 and 100")

while True:
	print("Guess a number:")
	guess = int(input())

	if guess < secretnumber:
		print("The number is higher")
	if guess > secretnumber:
		print("The number is lower")
	if guess == secretnumber:
		False
		break

if guess == secretnumber:
	print("You've guessed the correct number!")

