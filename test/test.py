import random
import sys 
import os
import pandas as pd
from scipy import stats  

#filename = input ("What file would you like to read in: ")
#print("Filename to be read in \'{}\'...".format(filename))
df = pd.read_csv('iris.txt', sep=',')

setosa = df[df['class'] == 'Iris-setosa']['sepal-length']
versicolor = df[df['class'] == 'Iris-versicolor']['sepal-length']
virginica = df[df['class'] == 'Iris-virginica']['sepal-length']

f_val, p_val = stats.f_oneway(setosa, versicolor, virginica)

print(p_val)

