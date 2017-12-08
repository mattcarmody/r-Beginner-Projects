#!/usr/bin/env python3
# proj08HigherLower.py - Beginner Project 8.
# https://www.reddit.com/r/beginnerprojects/comments/19jj9a/project_higherlower_guessing_game/

import random

def main():
	print("\nI'm thinking of a number somewhere between (and including) 1 to 100...")
	# Identify the target number
	jewel = random.randint(1, 100)
	# Initialize counter variable
	count = 0
	
	# Return higher or lower until the user guesses the target number
	while True:
		# User guesses a number
		guess = int(input("What do you think it is?\n"))
		# Update count
		count += 1
		if guess > jewel:		# Guess high
			print("Your guess is too high... try again.")
		elif guess < jewel:		# Guess low
			print("You guess is too low... try again.")
		else:				# Successful guess and break loop
			print("Congrats! You got it in " + str(count) + " tries.")
			break
			
# Tell user how the game works.
print("Have you ever played a higher lower guessing game? You try to guess my number and I tell you if your guess was too high or too low. Let's see how many guesses it takes!")
# Loop through the game until the user wants to stop.
while True:
	main()
	if input("Want to stop? Press Y.") == "Y":
		break


