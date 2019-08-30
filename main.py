import numpy as np                                          
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from loadData import loadData       

option = ''                         # used to navigate the menu
n = 0                               # size of data set
xInput = []                         # user input measurement to be classified by KNN
count = 0
k = 0
d = 0                               # of dimensions
Tk().withdraw()                     # we don't want a full GUI, so keep the root window from appearing

print('| ######################################################## |')
print('| Test knn function                                        |')
print('|                                                          |')
print('| Data must be in [X0,X1,...,Xn,Y] format with no headers  |')
print('| y-values as strings are acceptable                       |')
print('| ######################################################## |')

while option != '0':

    print('|\n| MAIN MENU ---------------------------------------------- ')
    print('| 1 - load data                          ',n,' rows loaded')
    print('| 2 - enter unclassified measurements    ',xInput,'')
    print('| 3 - enter k value                       k =',k)
    print('| 0 - exit')
    option = input('| > ')

    # print('knn(k,fileName')
    if option == '1':
        
        # fileName = askopenfilename()               SOMETIMES FREEZES!
        fileName = 'iris_csv.csv'

        print('| Loading data set...')
        loadedData = loadData(fileName)              # loads data, splits into y = last column, x = remaining columns, returns tuple (x,y)
        x = loadedData[0]
        y = loadedData[1]
        n = y.size                                   # n = number of data rows
        d = x[0].size                                # d = number of measured dimensions

        for i in x:                                  # data was retrieved as string to accomodate string y-values
            for j in i:
                j = float(j)

        x = x.reshape(n,d)                           # numpy cancer - necessary to use as arrays
        y = y.reshape(n,1)                           # x[n] gives you the nth array of measurements where the number of measurements = d
        print('| Dataset loaded.')                   # y[0][n] gives you the nth response variable

        xInput = []                                  # reset input measurements

    if option == '2':
        if d < 1:
            print('| Dataset not loaded. Load the dataset before entering unclassified data points.')
        else:
            print('| Input measurements:')                        # user inputs x-variable values
            while count < d:
                xIn = float(input('|\tx['+str(count+1)+'] = '))
                xInput.append(xIn)
                count += 1
    count = 0

    if option == '3':
        while k < 1:
            print('| Enter  positive value for k:')
            k = int(input('| > '))

    if option == '4':
        knnDist





