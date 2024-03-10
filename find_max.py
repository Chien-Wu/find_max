numbers = [1,3,5,7,9]

def find_max(numbers):
	max_number = numbers[0]
	for number in numbers:
		if number > max_number:
			max_number = number
	return max_number

max_number = find_max(numbers)
print(max_number)