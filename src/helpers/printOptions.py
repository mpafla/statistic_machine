

def printOptions(options, text=" "):
	if text != " ":
		text = " " + text + " "
	i = 0
	for option in options:
		print("Press {0} for{1}{2}".format(i, text, option))
		i = i + 1
