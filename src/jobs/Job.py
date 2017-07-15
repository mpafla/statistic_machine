

class Job:

	job_type = None

	def __init__(self, type):
		self.job_type = type

	def getJobType(self):
		return self.job_type

	def getInstruction(self, view, model):
		pass