import numpy as np                                          
import matplotlib.pyplot as plt
from loadData import loadData   
from knnDist import knnDist    

option = ''                         # used to navigate the menu
xInput = []                         # user input measurement to be classified by KNN
count = 0
k = 0
d = 0                               # of dimensions

fileName = 'iris_csv.csv'

loadedData = loadData(fileName)     # ML function returns tuple (Training Set, Test Set)
x = loadedData[0]
y = loadedData[1]

n = y.size                          # size of dataset
d = x[0].size                       # of dimensions

x = x.astype(np.float)              # data was retrieved as string to accomodate string y-values

xInput = [1.1,1.2,1.3,1.4]
k = 5

print(knnDist(xInput,x,k))