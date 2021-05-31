#This is where the code hits
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import os
import csv
#%matplotlib inline

data = pd.read_csv("../data/King_County_House_prices_dataset.csv")

file = open("../data/King_County_House_prices_dataset.csv")
reader = csv.reader(file, delimiter=',')
for row in reader:
    for column in row:
         for column2 in row:
            plot = data.plot(title=column+' '+column2 ,x = column, y= column2, kind='scatter', lw=2, colormap='jet')
            plot.set_xlabel(column)
            plot.set_ylabel(column2)
            plt.savefig('images/'+column+ '-vs-' + column2 + '.png')
    break