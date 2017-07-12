from views.InputTerminalView import *
from models.DataModel import *
from controller.InputController import *


def start():
	input_view = InputTerminalView()
	input_controller = InputController(input_view)
	model = DataModel()

start()