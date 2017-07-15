import random
import sys 
import os
from r_functions.readInputFile import readInputFile

class DataModel:

	df = None
	file_path = None
	job_type = None


	def loadDataFrame(self):
		self.df = readInputFile(self.file_path)

	def getDataFrame(self):
		return self.df

	def getJobType(self):
		return self.job_type

	def setFilePath(self, file_path):
		self.file_path = file_path

	def setJobType(self, job_type):
		self.job_type = job_type
