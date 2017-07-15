from r_functions.showHead import showHead
from views.InputView import *

class InputTerminalView(InputView):

	def getFilename(self):
		print ("Welcome to the Statistic Machine!")
		filename = input ("What file do you want to analyze? - ")
		print ("\nThe file to be analyzed: {}\n".format(filename))
		return filename

	def error(self, error):
		if (error == "loadDataFrame"):
			print("Data frame could not be loaded")