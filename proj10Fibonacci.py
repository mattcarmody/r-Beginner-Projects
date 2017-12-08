#!/usr/bin/env python3
# proj10Fibonacci.py - r/BeginnerProjects #10
# https://www.reddit.com/r/beginnerprojects/comments/19r3qg/functionfibonacci_sequence/

# Prompt user for integer input
n = int(input("What number in the sequence would you like?"))

# Initialize first two digits in Fibonacci sequence
fib = [0, 1]

# Append new digits to Fibonacci sequence up to the user input
for i in range(2, n):
	new = fib[i-2]+ fib[i-1]
	fib.append(new)
	
# Print nth integer in Fibonnaci sequence
print(fib[n-1])
