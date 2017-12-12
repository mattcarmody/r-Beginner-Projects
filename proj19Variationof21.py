#!/usr/bin/env python3
# proj19VariationOf21.py - r/BeginnerProjects # 19
# https://www.reddit.com/r/beginnerprojects/comments/19ot36/project_a_variation_of_21/
# Cards cannot be drawn twice in one hand, fresh deck is used for each hand

import random, numpy, time

fullDeck = [["Ace of Hearts", 1], 
		["2 of Hearts", 2],
		["3 of Hearts", 3],
		["4 of Hearts", 4],
		["5 of Hearts", 5],
		["6 of Hearts", 6],
		["7 of Hearts", 7],
		["8 of Hearts", 8],
		["9 of Hearts", 9],
		["10 of Hearts", 10],
		["Jack of Hearts", 10],
		["Queen of Hearts", 10],
		["King of Hearts", 10],
		["Ace of Diamonds", 1],
		["2 of Diamonds", 2],
		["3 of Diamonds", 3],
		["4 of Diamonds", 4],
		["5 of Diamonds", 5],
		["6 of Diamonds", 6],
		["7 of Diamonds", 7],
		["8 of Diamonds", 8],
		["9 of Diamonds", 9],
		["10 of Diamonds", 10],
		["Jack of Diamonds", 10],
		["Queen of Diamonds", 10],
		["King of Diamonds", 10],
		["Ace of Clubs", 1],
		["2 of Clubs", 2],
		["3 of Clubs", 3],
		["4 of Clubs", 4],
		["5 of Clubs", 5],
		["6 of Clubs", 6],
		["7 of Clubs", 7],
		["8 of Clubs", 8],
		["9 of Clubs", 9],
		["10 of Clubs", 10],
		["Jack of Clubs", 10],
		["Queen of Clubs", 10],
		["King of Clubs", 10],
		["Ace of Spades", 1],
		["2 of Spades", 2],
		["3 of Spades", 3],
		["4 of Spades", 4],
		["5 of Spades", 5],
		["6 of Spades", 6],
		["7 of Spades", 7],
		["8 of Spades", 8],
		["9 of Spades", 9],
		["10 of Spades", 10],
		["Jack of Spades", 10],
		["Queen of Spades", 10],
		["King of Spades", 10]]
	
	
def playHand(hand, handScore):
	# Deal out two cards
	hand, handScore = deal(hand, handScore)
	
	# Keep giving user the option to hit until he stays or busts
	while True:
		hitOrStay = input("Would you like to 'HIT' or 'stay'?")
		
		if hitOrStay == "HIT":
			hand, handScore = hit(hand, handScore)
			print("Your score is", handScore)
			if handScore <= 21:
				continue
			else:
				print("That was a bust!")
				break
		
		elif hitOrStay == "stay":
			break
		
		else:
			print("I don't understand, HIT or stay?")
			continue
	
	# Round score is always negative. It's the difference between hand score and 21 or 21 for a bust
	if handScore > 21:
		roundScore = -21
	else:
		roundScore = handScore - 21
	
	return roundScore
	

def deal(hand, handScore):
	# Deal out two cards
	handIndex = numpy.random.choice(52, size=2, replace=False)
	handIndex = list(handIndex)
	for i in handIndex:
		hand.append(fullDeck[i][0])
		handScore += fullDeck[i][1]

	# Print user's hand
	print("\nYour hand is:")
	for i in range(len(hand)):
		print(hand[i])
	print("You hand score is", handScore)
	
	
	return hand, handScore
	
def hit(hand, handScore):
	while True:
		# Draw a new card
		newCardIndex = int(numpy.random.choice(52, size=1))
		
		# If it's already in user's hand, draw again
		if newCardIndex in hand:
			continue
		
		else:
			hand.append(newCardIndex)
			handScore += fullDeck[newCardIndex][1]
			print("You drew a ", fullDeck[newCardIndex][0])
			break
	
	
	return hand, handScore


# Initialize and introduce game
gameScore = 100
rounds = 5
print("Welcome to a variation of 21. There are " + str(rounds) + " rounds. You start with " + str(gameScore) + " points. Good luck!")

# Loop through 5 hands
for i in range(rounds):
	hand = []
	handScore = 0
	gameScore += playHand(hand, handScore)
	time.sleep(2)

# Print results
if gameScore > 0:
	print("\n\nThat's the end, you survived 5 rounds of this variation of 21! Your total score was", gameScore)
else:
	print("\n\nYikes! You lost. That's tough to do. Your total score was", gameScore)
