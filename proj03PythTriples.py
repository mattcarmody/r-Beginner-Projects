#!/usr/env/bin python3
# proj03PythTriples.py - r/BeginnerProject #3
# https://www.reddit.com/r/beginnerprojects/comments/19jwi6/project_pythagorean_triples_checker/

sides = [0, 0, 0]

def triples():
	sides[0] = int(input("What's the length of side one?"))
	sides[1] = int(input("What's the length of side two?"))
	sides[2] = int(input("What's the length of side three?"))
	sides.sort()
	if sides[0]**2 + sides[1]**2 == sides[2]**2:
		print("Congrats! That's a triple.")
	else:
		print("Nope, not a triple.")
	
while True:	
	triples()
	feedback = input("Do you want to try again? Y/N")
	if feedback == "N":
		break
