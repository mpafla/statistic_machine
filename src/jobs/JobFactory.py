from jobs.LearnJob import *
from jobs.TestJob import *

class JobFactory:

	def createJob(self, job_type):
		if (job_type == "test"):
			return TestJob(job_type)
		elif (job_type == "learn"):
			return LearnJob(job_type)
