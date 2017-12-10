#!/usr/bin/env python3
# proj13DiceRoll.py - r/BeginnerProjects #13
# https://www.reddit.com/r/beginnerprojects/comments/1j50e7/project_dice_rolling_simulator/

import random, time

# Loop until keyboard interrupt
while True:
	try:
		# Prompt until a positive integer is input for num of sides
		while True:
			try:
				sides = int(input("How many sides does the die have?"))
			except ValueError:
				print("I need an integer!")
				continue
			if not sides > 0:
				print("I need a positive integer!")
			else:
				break
		# Prompt until a positive integer is input for num of rolls
		while True:
			try:
				rolls = int(input("How many times should it be rolled?"))
			except ValueError:
				print("I need an integer!")
				continue
			if not rolls > 0:
				print("I need a positive integer!")
			else:
				break
		
		# Initialize variables
		results = []
		resultsDict = {}

		# Random rolls
		for i in range(rolls):
			results.append(random.randint(1, sides))
	
		# Count appearance of each side of the die
		for i in results:
			if i in resultsDict:
				resultsDict[i] += 1
			else:
				resultsDict.setdefault(i, 1)

		# Print results and their percentages
		for k in resultsDict:
			print(str(k) + " appeared " + str(resultsDict[k]) + " times, or " + str(round(resultsDict[k]/rolls*100, 2)) + "% of the time.")
		
		# Pause, allowing time for keyboard interrupt, then begin again
		time.sleep(3)
		print("\nLet's go again!\n")
	
	# Break out of program
	except KeyboardInterrupt:
		print("This was fun.")
		break
