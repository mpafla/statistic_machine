import random
import sys 
import os
from r_functions.readInputFile import readInputFile

def loadDataFrame(filename):
	global df
	df = readInputFile(filename)

def getDataFrame():
	return df