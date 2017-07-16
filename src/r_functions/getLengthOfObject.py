import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from rpy2.robjects.vectors import DataFrame

r = robjects.r

def getLengthOfObject(object):
	return r.length(object)[0]