import random
import sys 
import os
from r_functions.showHead import showHead



def getFileName():
	print ("Welcome to the Statistic Machine!")
	filename = input ("What file do you want to analyze? - ")
	print ("The file to be analyzed: {}".format(filename))
	return filename

def peak(df):
	showHead(df)

