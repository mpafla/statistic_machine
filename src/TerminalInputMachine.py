import random
import sys 
import os
from r_functions.showHead import showHead
from InputMachine import *

class TerminalInputMachine(InputMachine):

	def getFilename(self):
		print ("Welcome to the Statistic Machine!")
		filename = input ("What file do you want to analyze? - ")
		print ("\nThe file to be analyzed: {}\n".format(filename))
		return filename

	def peak(self, df, number):
		print("Those are the first 5 rows to be analyzed:")
		showHead(df, number)

