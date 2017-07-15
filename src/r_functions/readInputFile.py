from pathlib import Path
import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from rpy2.robjects.vectors import DataFrame

r = robjects.r

def readInputFile(file_path):
	return DataFrame.from_csvfile(file_path, header=True, sep=',')


