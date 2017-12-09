#!/usr/bin/env python3
# proj15WhichNumber.py - r/BeginnerProjects #15
# https://www.reddit.com/r/beginnerprojects/comments/1dbena/challenge_whats_my_number/

# Potential changes:
# How can these steps be done in the most computationally efficient order? A wholly different approach?

candidates = []
candidates2 = []
candidates3 = []

# The number has two or more digits, starting range 10 - 1000
# The number does not contain a 1 or 7, starting range 20 - 1000
for i in range(20, 1001):
	if str(1) not in str(i) and str(7) not in str(i):
		candidates.append(i)
		
# The sum of all of the digits is less than or equal to 10
# AND the first two digits add up to be odd
# AND the second to last digit is even
# AND the last digit is equal to how many digits are in the number
for i in candidates:
	digitSum = 0
	iStr = str(i)
	for j in range(len(iStr)):
		digitSum += int(iStr[j])
	twoDigitSum = int(iStr[0]) + int(iStr[1])
	secondToLast = int(iStr[-2])
	if digitSum <= 10 and twoDigitSum % 2 == 1 and secondToLast % 2 == 0 and int(iStr[-1]) == len(iStr):
		candidates2.append(i)

# The number is prime
for i in candidates2:
	bucket = []
	for j in range(2, i):
		if i % j == 0:
			bucket.append(j)
	if len(bucket) == 0:
		candidates3.append(i)

print(candidates3)
print("There are two numbers that meet the criteria because the designer didn't realize 0 is an even number.")
