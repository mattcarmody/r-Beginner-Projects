#!/usr/bin/env python3
# proj14GreenEggsAndHam.py - r/BeginnerProjects #14
# https://www.reddit.com/r/beginnerprojects/comments/1i6sax/challenge_count_and_fix_green_eggs_and_ham/

# Source says the solution is 70 but I count 84, see proj14troubleshooter.py
# 57 - "\ni "
# 13 - "-i-"
# 13 - " i "
# 1 - first character in the file, no preceding character ("i ")

import re

# Read in txt file
storyFile = open('/home/matt/BeginnerProjects/proj14SamIAm.txt')
storyContent = storyFile.read()

# Create a regex to find i's that need changing
iRegex = re.compile(r'(\W)i(\W)')

# Sub uppercase I for lowercase and udpate counter
subOutput = iRegex.subn(r"\1I\2", storyContent)
newString = subOutput[0]
count = subOutput[1]

# TODO: Make this automatic
# Account for first/last characters (only applies to first in this case)
# Need to convert to list, replace it, then back again
firstCharList = list(newString)
firstCharList[0] = "I"
newString= "".join(firstCharList)
count += 1

# Save updated string to a new txt file
updatedStoryFile = open('proj14SamIAmUpdated.txt', 'w')
updatedStoryFile.write(newString)
updatedStoryFile.close()

# Print number of errors corrected
print(str(count) + " errors were corrected.")
