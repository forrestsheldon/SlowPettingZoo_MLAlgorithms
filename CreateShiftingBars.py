#This script creates a one dimentional shifting bar data set.
import numpy as np

def CreateShiftingBars(totLength, barLength):
    dataSet = np.zeros([totLength,totLength])
    for i in range(totLength):
        element = np.zeros(totLength)
        if i + barLength <= totLength:
            element[i:i+barLength] = 1
        else:
            element[i:totLength] = 1
            element[0:np.mod(i+barLength, totLength)] = 1
        dataSet[i,:] = element
    return dataSet

