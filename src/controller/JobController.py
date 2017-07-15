from views.JobTerminalView import *
from jobs.Job import *

class JobController:

	def __init__(self):
		self.view = JobTerminalView() 

	def createJob(self, model):
		job_type = self.view.getJobType()
		job = Job(job_type)
		return job
		

		