import numpy as np                                          
import matplotlib.pyplot as plt
from knn import knn
from splitData import splitData     # split data into training/testing sets                      
option = ''                         # used to navigate the menu
n = 0                               # size of data set
xInput = []                         # user input measurement to be classified by KNN
ratio = 0.66
count = 0
k = 0

print('| ######################################################## |')
print('| Test knn function                                        |')
print('|                                                          |')
print('| Data must be in [X0,X1,...,Xn,Y] format with no headers  |')
print('| y-values as strings are acceptable                       |')
print('| ######################################################## |')

while option != '0':

    print('|\n| MAIN MENU ---------------------------------------------- ')
    print('| 1 - load data                          ',n,' rows loaded')
    print('| 2 - change data set split ratio         ratio =',ratio)
    print('| 3 - enter unclassified measurements    ',xInput,'')
    print('| 4 - enter k value                       k =',k)
    print('| 0 - exit')
    option = input('| > ')

    # print('knn(k,fileName')
    if option == '1':
        fileName = 'iris_csv.csv'

        print('| Loading data set...')
        splitedData = splitData(fileName,ratio)                   # ML function returns tuple (Training Set, Test Set)

        xTest = (splitedData[1])[:,0:-1]                          # all the important info
        yTest = (splitedData[1])[:,-1]  
        y = (splitedData[0])[:,-1]            
        m = y.size
        n = yTest.size
        x = (splitedData[0][:,0:-1])
        d = x[0].size                                             # dimensions

        for i in xTest:                                           # data was retrieved as string to accomodate string y-values
            for j in i:
                j = float(j)
        for i in x:
            for j in i:
                j = float(j)

        x = x.reshape(m,d)                                        # numpy cancer - necessary to use as arrays
        y = y.reshape(m,1)
        xTest = xTest.reshape(n,d)      
        yTest = yTest.reshape(n,1)
        print('| Data set loaded.')

        xInput = []                                               # reset input measurements

    if option == '2':                                             # NEED TO ADD:  recalculate the loaded data set
        print('| 3 - enter unclassified measurements')
        print('| Enter new ratio as decimal value.')
        print('| (training set size):(test set size)')
        print('|       =(your value):(1 - your value)')
        ratio = input('| > ')

    if option == '3':
        print('| Input measurements:')                            # user inputs x-variable values
        while count < d:
            xIn = float(input('|\tx['+str(count+1)+'] = '))
            xInput.append(xIn)
            count += 1
    count = 0

    if option == '4':
        while k < 1:
            print('| Enter  positive value for k:')
            k = int(input('| > '))




