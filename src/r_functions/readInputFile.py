from pathlib import Path
import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from rpy2.robjects.vectors import DataFrame

r = robjects.r

def readInputFile(filename):
	path_string = "/home/marvinpafla/try/statistic_machine/data/"+filename
	path = Path(path_string)
	if (path.is_file()):
		df = DataFrame.from_csvfile(path_string, header=True, sep=',')
		return df
	else:
		return False

