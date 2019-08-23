import numpy as np                                        # aka MATLAB for poor people
import matplotlib.pyplot as plt                                       

from splitData import splitData                           # ML functions


option = ''

while option != '0':
    print('Test knn function')
    print('Data must be in [X0,X1,...,Xn,Y] format with no headers')
    print('y-values as strings are acceptable')
    print('function will detect number of traits measured in data')
    print('knn(k,fileName')

    ratio = 0.66                                          # user dependent variables

    # k = input('enter k-value\n > ')
    fileName = 'iris_csv.csv'

    splitedData = splitData(fileName,ratio)                # ML function returns tuple (Training Set, Test Set)

    xTest = (splitedData[1])[:,0:-1]                       # all the important info
    yTest = (splitedData[1])[:,-1]  
    y = (splitedData[0])[:,-1]            
    m = y.size
    n = yTest.size
    x = (splitedData[0][:,0:-1])
    d = x[0].size #dimensions

    for i in xTest:                                       # data was retrieved as string to accomodate string y-values
        i = float(i)
    for i in x:
        i = float(i)

    x = x.reshape(m,1)                                    # numpy cancer
    y = y.reshape(m,1)
    xTest = xTest.reshape(n,1)      
    yTest = yTest.reshape(n,1)

    option = input('1 to continue\n0 to exit\n > ')

