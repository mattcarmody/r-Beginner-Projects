#!/usr/bin/env python3
# proj17CountdownClock.py - r/BeginnerProjects # 17
# https://www.reddit.com/r/beginnerprojects/comments/1bvdmq/project_countdown_clock/

import datetime, time

# Ask user for a date, one part at a time
print("Give me a date and time and I'll start a countdown.\n")
year = int(input("What year?"))
month = input("What month?")
day = int(input("What day?"))
hour = int(input("What hour?"))
minute = int(input("What minute?"))
second = int(input("What second?"))

# Handle month input, allowing for text or integer
if month == "Jan" or month == "January":
	month = 1
elif month == "Feb" or month == "February":
	month = 2
elif month == "Mar" or month == "March":
	month = 3
elif month == "Apr" or month == "April":
	month = 4
elif month == "May" or month == "May":
	month = 5
elif month == "Jun" or month == "June":
	month = 6
elif month == "Jul" or month == "July":
	month = 7
elif month == "Aug" or month == "August":
	month = 8
elif month == "Sep" or month == "September":
	month = 9
elif month == "Oct" or month == "October":
	month = 10
elif month == "Nov" or month == "November":
	month = 11
elif month == "Dec" or month == "December":
	month = 12
else:
	month = int(month)

# Compile user target date
jewel = datetime.datetime(year, month, day, hour, minute, second)

# Get the current datetime
now = datetime.datetime.now()

print("Target time:")
print(jewel)
print("\nCurrent time:")
print(now)

# Countdown while target date is still in the future
while (jewel - now).total_seconds() >= 0:
	print('\nTime remaining:')
	print(jewel - now)
	print('')
	time.sleep(5)
	now = datetime.datetime.now()

# Tell user the time has passed
print("\nIt already happened, you missed it.")

