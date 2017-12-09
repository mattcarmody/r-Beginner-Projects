#!/usr/bin/env python3
# proj18Pokemon.py - r/BeginnerProjects #18
# https://www.reddit.com/r/beginnerprojects/comments/1aw0iq/project_turn_based_pokemon_style_game/

import random, time
import numpy as np
from numpy.random import choice

moves = ['strike', 'FURY', 'recovery']
strike = [18, 25]		# [min damage, max damage]
FURY = [10, 35]		# [min damage, max damage]
recovery = [18, 25]		# [min damage, max damage]
startingHealth = [100, 100]		# [starting user health, starting opponent health]

def main(userHealth, compHealth):
	while True:		# Loop through moves until game ends
		# Game status
		print("Your health is " + str(userHealth) + "\nOpponent health is " + str(compHealth) + "\n")
		
		# User chooses a move
		userMove = input("It's your move... choices are strike, FURY and recovery.")
		if userMove == 'strike':
			damage = random.randint(strike[0], strike[1])
			# TODO: Make damage points max out at their current health to make numbers add up clean (x4)
			print("You deal " + str(damage) + " damage points with strike!")
			compHealth -= damage
		elif userMove == 'FURY':
			damage = random.randint(FURY[0], FURY[1])
			print("You deal " + str(damage) + " damage points with FURY!")
			compHealth -= damage
		elif userMove == 'recovery':
			regen = random.randint(recovery[0], recovery[1])
			print("You regenerate " + str(regen) + " health points with recovery.")
			userHealth += regen
			userHealth = min(userHealth, 100)		# Prevents user health going above 100
		else:		# User input didn't match a move name
			print("I don't understand that move... try again.")
			continue
		
		# Brief hesitation between moves
		time.sleep(2)
		print('')
		
		# Checks computer health
		if compHealth <= 0:		# User wins
			print("Wow, you did it! GAME OVER YOU WON.")
			break
		elif compHealth < 35:	# Computer move probabilities change when health is under threshold
			prob = np.array([0.25, 0.25, 0.50])
			compMove = choice(moves, p = prob)
		else:				# Standard computer move, equal probability of each
			compMove = choice(moves)
		
		print("Your opponent plays move " + compMove + "...")
		
		# Computer makes move
		if compMove == 'strike':
			damage = random.randint(strike[0], strike[1])
			print("Your opponent deals you " + str(damage) + " damage points with strike!")
			userHealth -= damage
		elif compMove == 'FURY':
			damage = random.randint(FURY[0], FURY[1])
			print("Your opponent deals you " + str(damage) + " damage points with FURY!")
			userHealth -= damage
		elif compMove == 'recovery':
			regen = random.randint(recovery[0], recovery[1])
			print("Your opponent regenerates " + str(regen) + " health points with recovery.")
			compHealth += regen
			compHealth = min(compHealth, 100)	# Prevents computer health going above 100
		else:
			print("Your opponent's move crashed.")
			break
		
		# Checks to see if user still has health
		if userHealth <= 0:		# Computer wins
			print("You just got beat by a computer!")
			break
	userHealth = max(userHealth, 0)	# Prevents user health going below 0
	compHealth = max(compHealth, 0)	# Prevents computer health going below 0
	print("Final score\nYour health: " + str(userHealth) + "\nOpponent health: " + str(compHealth))
	
# Run function with starting health initialized above
main(startingHealth[0], startingHealth[1])

