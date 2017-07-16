

def getInputNumber(min, max, prompt):
	input_correct = False
	while (input_correct == False):
		try:
			number = int(input (prompt))
		except ValueError:
			print ("This is not a number.")
			continue
		if ((min <= number) and (number <= max)):
			return number
		else:
			print ("Number out of range.")
