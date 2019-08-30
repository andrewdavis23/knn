import numpy as np

def loadData(fileName):

    data = np.genfromtxt(fileName, dtype=str, comments='#', delimiter=',')

    x = data[:,0:-1]
    y = data[:,-1]

    return x, y
