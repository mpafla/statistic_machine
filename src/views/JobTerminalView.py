

class JobTerminalView:

	job_dict = {1 : "test", 2 : "learn"}

	def getJobType(self):
		job_type = False
		while (job_type == False):
			print("What kind of job would you like to execute?")
			print("Press")
			for key in self.job_dict:
				print ("Press {0} for {1} job".format(str(key), self.job_dict[key]))
			tmp = input ("Press number for job: ")
			if int(tmp) in self.job_dict:
				job_type = self.job_dict[int(tmp)]
				return job_type