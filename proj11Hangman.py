#!/usr/bin/env python3
# proj11Hangman.py - r/BeginnerProjects #11
# https://www.reddit.com/r/beginnerprojects/comments/1irw2j/project_hangman_game/

import random

# Create word list
words = "jump run skip snort snark smell rip ride pocket runner coaster jimminy cricket crock rock brand rump stump ripple grunge grease grime lurve rickety nimble ricket rickshaw rocket"
wordlist = words.split()

# Initialize empty lists for letters guessed correctly & incorrectly and initialize counter
missedLetters = []
correctLetters = []
count = 0

# Choose random word from list, create matching placeholder of underscores
jewel = random.choice(wordlist)
placeholder = "_" * len(jewel)

# Loop through guesses until game ends
while True:
	print(placeholder)
	guess = input("Guess a letter! (lowercase or input GIVE UP to quit.)\n")
	
	'''
	for i in range(len(jewel)):
		if guess in jewel[i]:
			correctLetters.append(guess)
	'''		
	
	
	if guess == "GIVE UP":	# User wants to exit mid-game
		print("Quitter! Quitter! All shame he who values his time.")
		break	
	elif len(guess) > 1:	# User inputs more than one letter at once
		print("That's too many letters, punk!")
	elif guess in correctLetters or guess in missedLetters:	# User repeats a guess
		print("You already guessed that! Try something new...")
	elif guess in jewel:	# User guesses a letter correctly
		print("Yep! Good guess.")
		correctLetters.append(guess)
		placeholder = ""
		for i in range(len(jewel)):	# Recreate placeholder with each guess
			if jewel[i] in correctLetters:
				placeholder += jewel[i]
			else:
				prompt += "_"
		if placeholder == jewel:		# User has guessed all the letters
			print("GAME OVER! YOU WON!")
			print("The word was " + placeholder)
			print("You only made " + str(count) + " mistake(s).")
			break	
	else:				# User guesses incorrectly
		print("Nope! Try again.")
		missedLetters.append(guess)
		count += 1
	
	# If count reaches 10, game is ended
	print("\n")
	if count >= 10:
		print("You're all out of guesses, that was 10.\n GAME OVER!")
		print("The word was " + jewel)
		break
