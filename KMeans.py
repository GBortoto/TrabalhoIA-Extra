from typing import List
import random
import math
import HarryPlotter as HP
from ListOfPoints import ListOfPoints

class KMeans():
    def __init__(self, dataPoints: ListOfPoints, NGroups):
        self.distances = ListOfPoints(len(dataPoints), NGroups, 100)
        self.done = False
        self.dataPoints = dataPoints
        self.centroids = ListOfPoints(NGroups, 2, 100)
        
        for i in range(NGroups):
            self.centroids.points[i] = [random.random()*self.centroids.maxRange for i in range(2)]
            

    def distance(self, pointA, pointB):
        # Eucledean Distance
        return math.sqrt(sum([math.pow(pointA[i] - pointB[i], 2) for i in range(len(pointA)-1)]))
            
    
    def calculate(self):
        while(not self.done):
            # Para cada ponto
            for i in range(len(self.dataPoints)):
                # e para cada centroide
                for j in range(len(self.centroids)):
                    #print('(i:' + str(i) + ', j:' + str(j) + ')')
                    self.distances.points[i][j] = self.distance(self.dataPoints.points[i], self.centroids.points[j])
            self.done = True
