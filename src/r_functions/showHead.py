import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from rpy2.robjects.vectors import DataFrame

r = robjects.r

def showHead(model, number):
	print(r.head(model.getDataFrame(), number))
