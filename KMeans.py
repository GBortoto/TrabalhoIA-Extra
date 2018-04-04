from typing import List
import random
import math
import HarryPlotter as HP
from ListOfPoints import ListOfPoints

class KMeans():
    def __init__(self, dataPoints: ListOfPoints, NGroups:int):
        # Lista de dados -> N * (x, y)
        self.dataPoints = dataPoints

        # Lista de centroides -> NGroups * (x, y)
        self.centroids = ListOfPoints(NGroups, 2, 100)

        # Lista de distâncias -> NGroups * (float)
        self.distances = [0.0 for i in range(NGroups)]

        # Lista de centróides mais proximos e seus respectivos clusters -> N * (x, y, ClusterID)
        self.nearest = ListOfPoints(len(dataPoints), 3, 100)

        # Setar posições aleatórias para os centróides
        for i in range(NGroups):
            self.centroids.points[i] = [random.random()*self.centroids.maxRange for i in range(2)]
            

    def distance(self, pointA, pointB):
        # Eucledean Distance
        return math.sqrt(
            sum(
                [(pointA[i] - pointB[i])**2 for i in range(len(pointA))]
                )
            )
    
    def findNearestCentroid(self):
        # Para cada ponto
        for i in range(len(self.dataPoints)):
            # e para cada centroide
            nearestCentroidIndex = 0
            for j in range(len(self.centroids)):
                
                #print('(i:' + str(i) + ', j:' + str(j) + ')')

                # Calcula a distância do centróide atual para o ponto atual
                self.distances[j] = self.distance(self.dataPoints.points[i], self.centroids.points[j])

                # Caso a distância calculada for menor do que a distância mínima já calculada 
                if(self.distances[j] <= self.distances[nearestCentroidIndex]):
                    # Então este centróide passa a ser o mais próximo
                    self.nearest.points[i] = [self.centroids.points[j][0], self.centroids.points[j][1], j]
                    # e a variável de index do centróide mais próximo é atualizada com a posição desse centroide na lista de centroides 
                    nearestCentroidIndex = j

    def recalculateCentroids(self):
        # Para cada centróide
        for i in range(len(self.centroids)):
            indexes_pointsInCluster = self.nearest.findAllPointsWith(i, 2).getDimention(3)
            pointsInCluster = ListOfPoints(len(indexes_pointsInCluster), 2, 100)
            for j in range(len(pointsInCluster)):
                pointsInCluster.points[j] = self.dataPoints.points[indexes_pointsInCluster[j]]

            #print('pointsInCluster')
            #print(pointsInCluster)
            
            meanX = sum(pointsInCluster.getDimention(0)) / len(pointsInCluster)
            meanY = sum(pointsInCluster.getDimention(1)) / len(pointsInCluster)
            
            self.centroids.points[i] = [meanX, meanY]

    def run(self):
        self.findNearestCentroid()
        self.recalculateCentroids()
