import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from rpy2.robjects.vectors import DataFrame

r = robjects.r

def readInputFile(filename):
	df = DataFrame.from_csvfile("/home/marvinpafla/try/statistic_machine/data/"+filename, header=True, sep=',')
	return df

