#!/usr/bin/env python3
# proj02Magic8Ball.py - r/BeginnerProjects #2
# https://www.reddit.com/r/beginnerprojects/comments/29aqox/project_magic_8_ball/

import time, random

responses = ["Nah.",
	"Get out of here.",
	"Could be, who knows man.",
	"Yes",
	"Technically your odds aren't zero, but realistically...",
	"Maybe.",
	"You're wasting everyone's time, ask me a real question.",
	"Totally",
	"I'm optimistic",
	"The future is cloudy"]
	
# Takes a question from user and, after a pause, returns a random response
def mainevent():
	# "Takes" a question from user but doesn't do anything with it
	input("Ask me a question")
	
	# Tells user it is thinking, waits for 3 seconds
	print("Let me think about that...")
	time.sleep(3)
	
	# Prints a random response from list above
	result = responses[random.randint(0,len(responses)-1)]
	print(result)

# Loop until user opts to quit program
while True:
	# Run 8 ball function
	mainevent()
	
	# Pause while user reads the 8 ball response
	time.sleep(3)
	
	# Give user the option to continue or quit
	prompt = input("Press anything to go again or enter QUIT\n")
	if prompt == "QUIT":
		break
