from r_functions.showHead import *

class TestController:

	def executeTest(self, job, model):
		showHead(model.getDataFrame(), 5)