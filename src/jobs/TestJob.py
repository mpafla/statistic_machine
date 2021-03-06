from jobs.Job import *

class TestJob(Job):

	independent_variable = None
	dependent_variable = None

	def __init__(self, job_type):
		super(TestJob, self).__init__(job_type)

	def getInstruction(self, view, model):
		self.independent_variable = view.getVariable(model, "What should be your independent variable?")
		self.dependent_variable = view.getVariable(model, "What should be your dependent variable?")

