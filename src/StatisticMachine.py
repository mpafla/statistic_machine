from views.InputTerminalView import *
from models.DataModel import *
from controller.InputController import *
from controller.LearnController import *
from controller.TestController import *
from controller.JobController import *
from controller.ExecuteController import *


def start():
	input_controller = InputController()
	model = DataModel()
	job_controller = JobController()
	execute_controller = ExecuteController()
	#output_controller = OutputController()

	if (input_controller.getInput(model)):
		job = job_controller.createJob(model)
		execute_controller.executeJob(job, model)
		#output_controller.printJob(result)

start()