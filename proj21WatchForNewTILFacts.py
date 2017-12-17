#!/usr/bin/python3
# proj21WatchforNewTILFacts.py - r/BeginnerProjects #21
# https://www.reddit.com/r/beginnerprojects/comments/1iqg6p/project_watch_for_new_til_facts/
# NOTE: does not use PRAW, so it's difficult to run. This was made based on outdated reddit API information and needs to be updated to be functional.

import json
import requests
import sys
import time

recent = []

def Check():
	url = "https://www.reddit.com/r/todayilearned/new.json"
	newTILJSON = requests.get(url, headers = {'customazzusername345754': 'yourbot4356747'})
	try:
		newTILJSON.raise_for_status()
	except:
		print("We've got a problem.")
		sys.exit()
	print("Scanning...")
	newTILDict = json.loads(newTILJSON.text)

	title = newTILDict["data"]["children"][0]["data"]["title"]
	if title.startswith("TIL that"):
		title = title[8:]
	if title.startswith("TIL"):
		title = title[4:]
	if title in recent:
		print("Nothing new here...")
	else:
		recent.append(title)
		print(title)


while True:
	Check()
	time.sleep(30)
