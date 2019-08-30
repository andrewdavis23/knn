import numpy as np
from operator import itemgetter

def knn(xInput,x,y,k):
    nIndex = []
    i = 0
    while i < k:
        print(min(enumerate(a), key=itemgetter(1))[0])
