from controller.LearnController import *
from controller.TestController import *

class ExecuteController:

	learn_controller = None
	test_controller = None

	def __init__(self):
		self.learn_controller = LearnController()
		self.test_controller = TestController()

	def executeJob(self, job, model):
		if (job.getJobType() == "test"):
			self.test_controller.executeTest(job, model)
		elif (job.getJobType() == "learn"):
			self.learn_controller.executeLearn(job, model)