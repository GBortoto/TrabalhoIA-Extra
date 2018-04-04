from HarryPlotter import HarryPlotter as HP
from ListOfPoints import ListOfPoints
from KMeans import KMeans
from random import random
import time
import sys
import _thread

def executeCode(a, b):
    for i in range(10, 100):
        time.sleep(0.5)
        data.points.append([random() * 100, random() * 100])

def hidePlotterOnDemand(plotter, b):
    text = ""
    while(text.lower() != 'p'):
        text = input("Para parar, digite p\n")
    plotter.close()
    

if __name__ == '__main__':
    print('Ponto 1')
    data = ListOfPoints(100, 2, 100)
    data.points = [[random()*100, random()*100] for i in range(100)]
    print('Ponto 2')
    kmeans = KMeans(data, 4)
    kmeans.calculate()
    print('Ponto 3')
    plotter = HP(kmeans.dataPoints, kmeans.centroids, kmeans.clusters)
    print('Ponto 4')
    
    try:
        #_thread.start_new_thread(executeCode, (0, 0))
        _thread.start_new_thread(hidePlotterOnDemand, (plotter, 0))
        print('Ponto 5')
        plotter.show()
        print('Ponto 6')
        
    except Exception as e:
        print(e)

    
