import random
import sys 
import os
from view import *
from model import *

def start():
	filename = getFileName()
	loadDataFrame(filename)
	df = getDataFrame()
	peak(df)


start()