from typing import List
import random
import math
import HarryPlotter as HP
from ListOfPoints import ListOfPoints

class KMeans():
    def __init__(self, dataPoints: ListOfPoints, NGroups):
        self.dataPoints = dataPoints
        self.centroids = ListOfPoints(NGroups, 2, 100)
        self.distances = ListOfPoints(len(dataPoints), NGroups, 100)
        self.nearest = ListOfPoints(len(dataPoints), 2, 100)
        self.clusters = ListOfPoints(len(dataPoints), 1, NGroups)
        self.done = False        
        
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
                nearestCentroidIndex = 0
                for j in range(len(self.centroids)):
                    
                    #print('(i:' + str(i) + ', j:' + str(j) + ')')

                    # Calcula a distância do centróide atual para o ponto atual
                    self.distances.points[i][j] = self.distance(self.dataPoints.points[i], self.centroids.points[j])

                    # Caso a distância calculada for menor do que a distância mínima já calculada 
                    if(self.distances.points[i][j] <= self.distances.points[i][nearestCentroidIndex]):
                        # Então este centróide passa a ser o mais próximo
                        self.nearest.points[i] = self.centroids.points[j]
                        # e a variável de index do centróide mais próximo é atualizada com a posição desse centroide na lista de centroides 
                        nearestCentroidIndex = j

                # Depois de encontrar o centróide mais proximo, atribua o ponto ao cluster representado pelo centróide mais próximo
                self.clusters.points[i] = j

            # Para cada cluster
            for i in range(len(self.centroids)):
                # Recalcular a posição do centróide referente a este cluster através da média da posição de todos os pontos atribuidos a este cluster
                self.centroids.points[i] = [sum(self.centroids.getDimention(0))/len(self.centroids),
                                            sum(self.centroids.getDimention(1))/len(self.centroids)]

            self.done = True
