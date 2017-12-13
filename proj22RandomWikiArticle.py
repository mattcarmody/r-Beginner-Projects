#!/usr/bin/python3
# proj22RandomWikiArticle.py - r/BeginnerProjects #2
# https://www.reddit.com/r/beginnerprojects/comments/1jg2ru/project_random_wikipedia_article/

import json, requests, sys, webbrowser

# Get information from wikipedia API
urlSrc = "https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json"
wikiRandGet = requests.get(urlSrc, headers = {'omycustomazzusername1': 'oyourbot1'})
try:
	wikiRandGet.raise_for_status()
except:
	print("There was a problem. Maybe wikipedia json has been called too many times or the link is no good.")
	sys.exit()
wikiRandData = json.loads(wikiRandGet.text)

# Loop through random pages, giving user the option to view them	
for i in range(10):
	title = wikiRandData["query"]["random"][i]["title"]
	response = input("Do you want to see " + title + "? Y to see it, Enter to skip, QUIT to stop")
	if response == "Y":
		urlDest = "https://en.wikipedia.org/wiki/" + title
		webbrowser.open(urlDest)
	elif response == "QUIT":
		print("Ok we're done here!")
		sys.exit()
	else:
		continue
print("You ran out of choices!")

