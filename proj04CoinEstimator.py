#!/usr/env/bin python3
# proj04CoinEstimator.py - r/BeginnerProject #4
# https://www.reddit.com/r/beginnerprojects/comments/1idqw1/project_coin_estimator_by_weight/

import math

# Weight of each coin in grams.
weights = {'penny': 2.5, 'nickel': 5, 'dime': 2.268, 'quarter': 5.67, 'half dollar': 11.34, 'dollar': 8.1}

# Number of each coin per roll.
rolls = {'penny': 50, 'nickel': 40, 'dime': 50, 'quarter': 40, 'half dollar': 20, 'dollar': 25}

# Worth of each coin.
worth = {'penny': .01, 'nickel': .05, 'dime': .10, 'quarter': .25, 'half dollar': .50, 'dollar': 1.00}

coinType = input("What type of coin do you have?")
weightUnit = input("Do you use grams or pounds? g/lb")
coinWeight = float(input("How much do they weigh?"))

if weightUnit != "g" and weightUnit != "lb":
	print("I don't recognize your unit, I'm rather stupid. Please try again.")
else:
	if weightUnit == "lb":
		coinWeight = coinWeight * 453.592
	if coinType in weights:
		coinQuant = round(coinWeight / weights[coinType])
		rollQuant = math.floor(coinQuant / rolls[coinType]) 	# Rounds down number of wrappers, since you can't fill it.
		print("I recommend " + str(rollQuant) + " wrappers.\nThat is because you have " + str(coinQuant) + " coins.\nThey're worth $" + str(coinQuant * worth[coinType]))
	else:
		print("I don't recognize that coin name, I'm rather stupid. Please try again.")
