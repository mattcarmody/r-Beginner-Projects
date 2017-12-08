#!/usr/env/bin python3
# proj06ChangeCalculator.py - Beginner Project 5.
# https://www.reddit.com/r/beginnerprojects/comments/19jkn8/project_change_calculator/

import math, time

# Loop until user breaks via price of 0
while True:
	# Prompt user for total price
	price = float(input("What is the total price? (0 to end the program)"))
	# End program if user inputs 0
	if price == 0.0:
		break
	# Prompt user for total paid by customer
	payment = float(input("How much were you given?"))
	
	diff = payment - price
	
	if diff < 0:		# Customer didn't pay enough
		print("He didn't give you enough money!\n")
	elif diff == 0:	# Customer paid in exact change
		print("Exact change, he can be on his way.\n")
	else:			# Customer paid too much, calculate change
		# Calculate number of dollars
		numDollars = math.floor(diff / 1)
		diff = round(diff - numDollars * 1, 2)
		# Calculate number of quarters
		numQuarters = math.floor(diff / .25)
		diff = round(diff - numQuarters * .25, 2)
		# Calculate number of dimes
		numDimes = math.floor(diff / .1)
		diff = round(diff - numDimes * .1, 2)
		# Calculate number of nickels
		numNickels = math.floor(diff / .05)
		diff = round(diff - numNickels * .05, 2)
		# Calculate number of pennies
		numPennies = math.floor(diff / .01)
		diff = round(diff - numPennies * .01, 2)
		
		if diff == 0:	# Verify all change due is accounted for
			print("Give the following:\n" + str(numDollars) + " dollars\n" + str(numQuarters) + " quarters\n" + str(numDimes) + " dimes\n" + str(numNickels) + " nickels\n" + str(numPennies) + " pennies\n")
		else:		# Something went wrong, not all change due is accounted for
			print("Something went horribly wrong! diff = " + str(diff))
	
	# Give a few second pause and start again
	time.sleep(3)
			
