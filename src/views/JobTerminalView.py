from r_functions.getColumns import *

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

	def getIndependentVariable(self, model):
		getColumns(model)
		print("What should be your independent variable?")

	def getDependentVariable(self, model):
		pass