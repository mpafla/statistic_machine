import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from rpy2.robjects.vectors import DataFrame
from rpy2.robjects import Formula

r = robjects.r

df = DataFrame.from_csvfile('iris.txt', header=True, sep=',')
formula = Formula('sepal_length ~ class')
fit = r.aov(formula, data=df)
print(r.summary(fit))
