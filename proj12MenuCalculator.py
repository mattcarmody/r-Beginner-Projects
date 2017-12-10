#!/usr/bin/env python3
# proj12MenuCalculator.py - r/BeginnerProjects #12
# https://www.reddit.com/r/beginnerprojects/comments/1bytu5/projectmenu_calculator/

import time

menu = [["Chicken Strips", 3.50], ["French Fries", 2.50], ["Hamburger", 4.00], ["Hotdog", 3.50], ["Large Drink", 1.75], ["Medium Drink", 2.25], ["Milk Shake", 2.25], ["Salad", 3.75], ["Small Drink", 1.25]]

# Convert menu to a pretty string
menuString = ""
for i in range(len(menu)):
	menuString += str(i + 1) + ". " + menu[i][0] + " - $" + str(menu[i][1]) + "\n"


def order():
	orderList = []
	orderDict = {}
	price = 0.0
	
	# Take order in string of digits
	orderStr = input("Enter an order string, consecutive numbers.")
	
	# Convert string to a list
	for i in range(len(orderStr)):
		orderList.append(orderStr[i])
	#orderList = sorted(orderList)
	
	# Sum up and print the total price
	for i in range(len(orderList)):
		price += float(menu[int(orderList[i])-1][1])
	print("\nTotal price is: $" + str(price))
	
	# Convert order to a counted dictionary
	for i in orderList:
		if i in orderDict:
			orderDict[i] += 1
		else:
			orderDict.setdefault(i, 1)
			
	# Print counted order in a pretty way
	print("\nThis order has:\n")
	for i in orderDict:
		print(str(orderDict[i]) + ": " + str(menu[int(i)-1][0]))
	print("\n")

# Loop through program until keyboard interrupt
try:
	while True:
		print(menuString)
		order()
		time.sleep(5)
except KeyboardInterrupt:
	print("Call it a day!")



