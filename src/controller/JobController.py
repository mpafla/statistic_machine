from views.JobTerminalView import *
from jobs.JobFactory import *
from r_functions.showHead import *

class JobController:

	def __init__(self):
		self.view = JobTerminalView() 
		self.factory = JobFactory()

	def createJob(self, model):
		job_type = self.view.getJobType()
		job = self.factory.createJob(job_type)
		showHead(model, 5)
		job.getInstruction(self.view, model)
		return job
		

		