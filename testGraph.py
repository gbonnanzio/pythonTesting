#! Program Files (x86)/PythonDownload/python
import matplotlib.pyplot as plt
def myGraph(x,y):
    plt.plot(x,y)
    plt.show()
    return 0

def determineY(x):
    length = len(x)
    y = []
    for i in range(length):
        y.append(x[i]**2) 
    return y

ourX = range(-20,21)
ourY = determineY(ourX)
myGraph(ourX,ourY)

