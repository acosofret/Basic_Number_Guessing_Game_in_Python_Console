from art import logo
import random
print(logo)
print("\nWelcome to the GUESS THE NUMBER Game !")
THE_NUMBER = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")
print(f"\n(Pssst...the correct answer is {THE_NUMBER})\n")
attempts = 0
level = input("Choose a difficulty. Type 'easy' or 'hard':\n")
while level != "easy" and level != "hard":
	print("Invalid level entered.")
	level = input("Choose a difficulty. Type 'easy' or 'hard':\n")
if level == "easy":
	attempts = 10
elif level == "hard":
	attempts = 5
# so far we presented the game, ask for desired level & adjusted the no. of attempts
guess = 0
while guess != THE_NUMBER and attempts > 0:
	# put the running function below:
	print(f"You have {attempts} attempts remaining to guess the number.")
	guess = int(input("Make a guess: "))
	attempts -= 1
	if guess < THE_NUMBER:
		print("Too low.\nGuess again.")
	elif guess > THE_NUMBER:
		print("Too high.\nGuess again")
# put the running function above
if guess == THE_NUMBER:
	print(f"You won! The number was {guess}")
elif attempts == 0:
	print("GAME OVER")

# IMPROVEMENTS:
# # * clear screen for each game instance
# # * ask if they want to play again
# # * console graphics could be added for winning or loosing

# BUGS:
# # * error when user input is different than integer type. Should check and ask again.