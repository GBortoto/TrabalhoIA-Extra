from HarryPlotter import HarryPlotter as HP
from ListOfPoints import ListOfPoints
from KMeans import KMeans
from random import random
import time
import sys
import _thread
import math

def executeCode(kmeans, timeVariable):
    #time.sleep(timeVariable)
    for i in range(99):
        #time.sleep(timeVariable)
        print('iteração ' + str(i+2))
        kmeans.run()
    
def hidePlotterOnDemand(plotter, b):
    text = ""
    while(text.lower() != 'p'):
        text = input("Para parar, digite p\n")
    plotter.close()
    

if __name__ == '__main__':
    
    n = 50000
    NGroups = 6

    
    timeVariable = math.log(n, 5) - 1.8
    data = ListOfPoints(n, 2, 100)
    data.points = [[random()*100, random()*100] for i in range(n)]
    kmeans = KMeans(data, NGroups)
    print('Iteração 1')
    kmeans.run()
    plotter = HP(kmeans.dataPoints, kmeans.centroids, kmeans.nearest, 1000 * timeVariable)
    
    try:
        #_thread.start_new_thread(executeCode, (kmeans, timeVariable))
        executeCode(kmeans, timeVariable)
        plotter.show()
        #_thread.start_new_thread(hidePlotterOnDemand, (plotter, 0))
        #plotter.show()
        
    except Exception as e:
        print(e)

    
