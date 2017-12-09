#!/usr/env/bin python3
# proj07MeanMedianMode.py - r/BeginnerProjects #7
# https://www.reddit.com/r/beginnerprojects/comments/1eqt8i/function_mean_median_and_mode/

def mean():
	total = 0
	for i in numbers:
		total += i
	return total / len(numbers)
	
def median():
	# Find median if list has an even length (mid-way point between two closest values)
	if len(numbers) % 2 == 0:
		median = (numbers[int(len(numbers) / 2 - 1)] + numbers[int(len(numbers) / 2)]) / 2
	# Find median if length has an odd length
	else:
		median = numbers[int(len(numbers) / 2)] # int used to round down
	return median
	
def mode():
	numdic = {}
	modes = []
	
	# Create a dictionary of the count for each number in the list
	for i in numbers:
		if i in numdic:
			numdic[i] += 1
		else:
			numdic.setdefault(i, 1)

	# Sort list
	sortednumdic = [(k, numdic[k]) for k in sorted(numdic, key=numdic.get, reverse=True)]

	# Identify and return the mode(s)
	modes.append(sortednumdic[0][0])
	# Check for and append if there is more than one mode
	for i in range(1, len(sortednumdic)):
		if sortednumdic[i][1] == sortednumdic[0][1]:
			modes.append(sortednumdic[i][0])
		else:	# Break once a value unequal to the first is found (values are sorted)
			break
	return modes
	
# Prompt user for numbers and create a sorted list
numbers = sorted([int(x) for x in input("Enter numbers separated by a space.").split()])

# Compute and print the mean
mean = mean()
print("The mean is " + str(mean))

# Compute and print the median
median = median()
print("The median is " + str(median))

# Compute and print the mode
mode = mode()
print("The mode is " + str(mode))
