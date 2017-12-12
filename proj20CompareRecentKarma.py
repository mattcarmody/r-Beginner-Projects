#!/usr/bin/python3
# proj20CompareRecentKarma.py - r/BeginnerProjects #20
# https://www.reddit.com/r/beginnerprojects/comments/1i951e/project_compare_recent_karma/

import json, requests, time, sys

# TODO: Figure out how to ping reddit more frequently.
# TODO: Add in error handling for if a user has less than 15 posts.

# Get json data from reddit and extract the score of recent posts
def user(username):
	url = "https://www.reddit.com/user/" + username + ".json"
	print("\n" + username)
	userGet = requests.get(url, headers = {'omycustomazzusername1': 'oyourbot1'})
	try:
		userGet.raise_for_status()
	except:
		print("There was a problem. Maybe reddit json has been called too many times or the username is no good.")
		sys.exit()
	userData = json.loads(userGet.text)
	
	userTotalScore = 0
	for i in range(15):
		recentScore = userData["data"]["children"][i]["data"]["score"]
		userTotalScore += recentScore
	print("Total score of " + str(userTotalScore) + " for the 15 most recent posts.")
	return userTotalScore

# User 1
username1 = input("Enter the first username:")
user1TotalScore = user(username1)
	
# Wait a bit, Reddit API gets upset
print("Waiting, bear with me...")
time.sleep(10)

# User 2
username2 = input("Enter the second username:")
user2TotalScore = user(username2)

# Final scoring
print("")
if user1TotalScore > user2TotalScore:
	print(username1 + " wins over " + username2 + " by a margin of " + str(user1TotalScore - user2TotalScore))
elif user1TotalScore < user2TotalScore:
	print(username2 + " wins over " + username1 + "by a margin of " + str(user2TotalScore - user1TotalScore))
else:
	print("It's a tie!")
