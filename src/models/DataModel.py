import random
import sys 
import os
from r_functions.readInputFile import readInputFile

class DataModel:

	df = None
	filename = None
	job_type = None


	def loadDataFrame(self):
		self.df = readInputFile(self.filename)
		return self.df

	def getDataFrame(self):
		return self.df

	def getJobType(self):
		return self.job_type

	def setFilename(self, filename):
		self.filename = filename

	def setJobType(self, job_type):
		self.job_type = job_type
