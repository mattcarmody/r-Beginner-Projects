#! /usr/bin/python3
# proj05MadLibs.py - r/BeginnerProjects #5
# https://www.reddit.com/r/beginnerprojects/comments/1i8vt5/project_mad_libs_story_maker/
# Adapted from a practice project in How to Automate the Boring Stuff with Python, by Al Sweigert. This version reads in from a .txt file, prints an updated story to the user and also writes out to a .txt file.

import re

# Create a base story string and convert it to a list
textContent = "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events. Another NOUN, though ADJECTIVE, went to VERB."
textWords = list(textContent.split())

# Define and run regex to recognize placeholders in list
madLibRegex = re.compile(r'''(
    ADJECTIVE |
    VERB |
    NOUN |
    ADVERB
    )''', re.VERBOSE)
mo = madLibRegex.findall(textContent)

# For each placeholder, call for user to input a replacement word of that class
for i in range(len(textWords)):
    if madLibRegex.match(textWords[i]):
        # Handle scenarios in which match ends with punctuation
        if textWords[i].endswith('.'):
            sub = (str(input("Enter your own " + textWords[i][:-1].lower() +": ")) + '.')
        elif textWords[i].endswith(','):
            sub = (str(input("Enter your own " + textWords[i][:-1].lower() +": ")) + ',')
        else:
            sub = (str(input("Enter your own " + textWords[i].lower() +": ")))
        # Remove placeholder, insert user word
        textWords.remove(textWords[i])
        textWords.insert(i, sub)
    else:
        continue

# Convert updated list to a string       
space = ' '
newSentence = space.join(textWords)

# Print updated list to user
print(newSentence)
