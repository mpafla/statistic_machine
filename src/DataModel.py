import random
import sys 
import os
from r_functions.readInputFile import readInputFile

class DataModel:

	def loadDataFrame(self, filename):
		global df
		df = readInputFile(filename)
		if (df == False):
			print("DataSet not found")

	def getDataFrame(self):
		return df