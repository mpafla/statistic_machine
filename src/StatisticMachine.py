import random
import sys 
import os
from InputMachine import *
from TerminalInputMachine import *
from model import *

peak_number = 5

def start():
	input_machine = TerminalInputMachine()
	filename = input_machine.getAllInput()
	loadDataFrame(filename)
	df = getDataFrame()
	input_machine.peak(df, peak_number)


start()