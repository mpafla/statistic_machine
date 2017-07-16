from r_functions.getColumnNames import *
from r_functions.getLengthOfObject import *
from helpers.getInputNumber import *
from helpers.printOptions import *

class JobTerminalView:

	job_dict = {1 : "test", 2 : "learn"}

	def getJobType(self):
		job_type = False
		while (job_type == False):
			print("What kind of job would you like to execute?")
			for key in self.job_dict:
				print ("Press {0} for {1} job".format(str(key), self.job_dict[key]))
			try: 
				key = int(input ("Press number for job: "))
			except ValueError:
				print ("This is not a valid number.")
				continue
			if key in self.job_dict:
				job_type = self.job_dict[int(key)]
				return job_type

	def getVariable(self, model, question):
		colnames = getColumnNames(model)
		number_of_colnames = getLengthOfObject(colnames)
		print (question)
		printOptions(colnames, "for column")
		return getInputNumber(0, number_of_colnames - 1, "Pick a number for a column: ")


	