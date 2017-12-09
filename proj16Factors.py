#!/usr/bin/env python3
# proj16Factors.py - r/BeginnerProjects #16
# https://www.reddit.com/r/beginnerprojects/comments/1a0d82/function_factors_of_a_number/

def factor(num):
	# Initialize empty list of factors
	factorList = []

	# Try every number up to num, appending when modulus == 0
	for i in range(1, num+1):
		if (num % i) == 0:
			factorList.append(i)
	
	# Return list of factors
	return factorList


# Prompt user for integer input
num = int(input("Give me a number, I'll give you the factors:\n"))

# Run factor function, printing output
print(factor(num))
