#!/usr/bin/env python3
# proj01BottlesofBeer.py - r/BeginnerProjects #1.
# https://www.reddit.com/r/beginnerprojects/comments/19kxre/project_99_bottles_of_beer_on_the_wall_lyrics/

for i in range(99, 2, -1):
	print(str(i) + " bottles of beer on the wall, " + str(i) + " bottles of beer! Take one down, pass it around, " + str(i-1) + " bottles of beer on the wall!\n")
	
for i in range(2, 1, -1):
	print(str(i) + " bottles of beer on the wall, " + str(i) + " bottles of beer! Take one down, pass it around, " + str(i-1) + " bottle of beer on the wall!\n")
	
for i in range(1, 0, -1):
	print(str(i) + " bottle of beer on the wall, " + str(i) + " bottle of beer! Take one down, pass it around, " + str(i-1) + " bottles of beer on the wall!\n")
