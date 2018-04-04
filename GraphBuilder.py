from HarryPlotter import HarryPlotter as HP
from ListOfPoints import ListOfPoints
from KMeans import KMeans
from random import random
import time
import sys
import _thread

def executeCode(kmeans, plotter):
    time.sleep(1.5)
    for i in range(29):
        time.sleep(1.5)
        print('iteração ' + str(i+2))
        kmeans.run()
        #print(kmeans.centroids)
        '''
        plotter.data = kmeans.dataPoints
        plotter.centroids = kmeans.centroids
        plotter.nearest = kmeans.nearest
        '''
        
def hidePlotterOnDemand(plotter, b):
    text = ""
    while(text.lower() != 'p'):
        text = input("Para parar, digite p\n")
    plotter.close()
    

if __name__ == '__main__':
    #print('Ponto 1')
    n = 500
    data = ListOfPoints(n, 2, 100)
    data.points = [[random()*100, random()*100] for i in range(n)]
    #print('Ponto 2')
    kmeans = KMeans(data, 4)
    print('Iteração 1')
    kmeans.run()
    #print('Ponto 3')
    #plotter= None
    plotter = HP(kmeans.dataPoints, kmeans.centroids, kmeans.nearest, 500)
    #print('Ponto 4')
    
    try:
        _thread.start_new_thread(executeCode, (kmeans, plotter))
        #_thread.start_new_thread(hidePlotterOnDemand, (plotter, 0))
        #print('Ponto 5')
        plotter.show()
        #print('Ponto 6')
        
    except Exception as e:
        print(e)

    
