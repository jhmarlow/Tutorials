# Different data loading methods

# Imports
import numpy as np
import csv

with open('Stock.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

    myFile = np.genfromtxt('Stock.csv', delimiter=',')

array = np.random.random((36, 36))
array1 = np.random.random((36, 10))