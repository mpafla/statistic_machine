import random
import sys 
import os
from InputMachine import *
from TerminalInputMachine import *
from DataModel import *


peak_number = 5

def start():
	input_machine = TerminalInputMachine()
	model = DataModel()
	filename = input_machine.getFilename()
	model.loadDataFrame(filename)




start()