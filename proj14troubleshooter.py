#!/usr/bin/env python3
# proj14GreenEggsAndHam.py - r/BeginnerProjects #14
# https://www.reddit.com/r/beginnerprojects/comments/1i6sax/challenge_count_and_fix_green_eggs_and_ham/

import re

# GOAL: Verify correct number of edits. Source says 70, I count 84

# Read in txt file
storyFile = open('/home/matt/BeginnerProjects/proj14SamIAm.txt')
storyContent = storyFile.read()

'''
# Regex 1: all
regex1 = re.compile(r'(\W)i(\W)')
subOutput1 = regex1.subn(r"\1I\2", storyContent)
newString1 = subOutput1[0]
count1 = subOutput1[1]
'''

# Regex 2: space i space
regex2 = re.compile(r' i ')
subOutput2 = regex2.subn(r" I ", storyContent)
newString2 = subOutput2[0]
count2 = subOutput2[1]

# Regex 3: -i-
regex3 = re.compile(r'-i-')
subOutput3 = regex3.subn(r"-I-", storyContent)
newString3 = subOutput3[0]
count3 = subOutput3[1]

# Regex 4: \ni-
regex4= re.compile(r'\ni ')
subOutput4 = regex4.subn(r"\nI ", storyContent)
newString4 = subOutput4[0]
count4 = subOutput4[1]

'''
# Save updated string to a new txt file
updatedStoryFile = open('proj14troubleshooter.txt', 'w')
updatedStoryFile.write(newString2)
updatedStoryFile.close()
'''

# Print number of errors corrected
#print(str(count1) + " errors were corrected.")
print(str(count2) + " errors were corrected by regex2, space i space.")
print(str(count3) + " errors were corrected by regex3, -i-.")
print(str(count4) + " errors were corrected by regex3, new line i space.")
print("Plus the first character misses the usual regex.")
