import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from rpy2.robjects.vectors import DataFrame

r = robjects.r

def getColumns(model):
	colnames = r.colnames(model.getDataFrame())
	i = 0
	for col in colnames:
		print("Press {0} for the variable {1}".format(i, col))
		i = i + 1