import numpy as np
import math

def knnDist(xInput, x, k):

    dist = []
    tempDist = 0
    c = 0

    for i in x:
        for j in i:
            tempDist += math.pow(j,2) + math.pow(xInput[c],2)
            c += 1
        dist.append(tempDist)    
        c = 0
        tempDist = 0

    return dist
