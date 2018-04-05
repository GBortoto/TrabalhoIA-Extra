import matplotlib.pyplot as plt
import matplotlib.animation as animation
#from matplotlib import style
from ListOfPoints import ListOfPoints
import time
import _thread
import sys
import random

class HarryPlotter():
    def __init__(self, dataPoints:ListOfPoints, centroids:ListOfPoints, nearest:ListOfPoints, maxRange:int, refreshRate:int=1000):
        """Recebe um ListOfPoints e cria um gráfico dinâmico"""
        # Cria ambiente onde o plot acontecerá
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1, 1, 1)

        # Cria uma referência aos ListOfPoints
        self.dataPoints = dataPoints
        self.centroids = centroids
        self.nearest = nearest
        self.maxRange = maxRange

        self.firstPlot = 5

        self.colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

        # Seta uma função de animação ao ambiente atual que atualiza a cada "refreshRate" milésimos
        self.ani = animation.FuncAnimation(self.fig, self.animate, refreshRate)

        #print(self.dataPoints.points[0], )

    def animate(self, i):
        """Função que é executada a cada iteração da animação, conforme o refreshRate"""
        # Limpar gráfico
        self.ax1.clear()

        #print(self.dataPoints)

        if(self.firstPlot > 0):
            self.ax1.plot(self.dataPoints.getDimention(0), self.dataPoints.getDimention(1), 'ko')
            '''
            for i in range(len(self.dataPoints)):
                self.ax1.plot(self.dataPoints.points[i][0], self.dataPoints.points[i][1], 'ko')
            '''
            self.firstPlot = self.firstPlot - 1
            return

        groups = [[] for i in range(len(self.centroids))]

        for i in range(len(self.dataPoints)):
            groups[self.nearest.points[i][2]].append([self.dataPoints.points[i][0],
                                                      self.dataPoints.points[i][1]])

        #print(groups)
        
        for i in range(len(self.centroids)):
            self.ax1.plot([groups[i][p][0] for p in range(len(groups[i]))],
                          [groups[i][p][1] for p in range(len(groups[i]))],
                          self.colors[i%len(self.colors)]+'o')
        '''
        self.ax1.plot([group1[i][0] for i in range(len(group1))],
                      [group1[i][1] for i in range(len(group1))],
                      'go')
        self.ax1.plot([group2[i][0] for i in range(len(group2))],
                      [group2[i][1] for i in range(len(group2))],
                      'bo')
        
        self.ax1.plot([group3[i][0] for i in range(len(group3))],
                      [group3[i][1] for i in range(len(group3))],
                      'yo')
        '''
        
        styles = ['r-', 'g-', 'b-', 'y-']
        for i in range(len(self.centroids)):
            indexes_pointsInCluster = self.nearest.findAllPointsWith(i, 2).getDimention(3)
            pointsInCluster = ListOfPoints(len(indexes_pointsInCluster), 2, self.maxRange)
            for j in range(len(pointsInCluster)):
                pointsInCluster.points[j] = self.dataPoints.points[indexes_pointsInCluster[j]]

            xType1 = pointsInCluster.getDimention(0)
            xType2 = self.nearest.findAllPointsWith(i, 2).getDimention(0)
            yType1 = pointsInCluster.getDimention(1)
            yType2 = self.nearest.findAllPointsWith(i, 2).getDimention(1)

            for j in range(len(pointsInCluster)):
                self.ax1.plot([xType1[j], xType2[j]],
                              [yType1[j], yType2[j]],
                              self.colors[i%len(self.colors)]+'-')
            '''
            self.ax1.plot([pointsInCluster.getDimention(0)],
                          [pointsInCluster.getDimention(1)],
                          [self.nearest.findAllPointsWith(i, 2).getDimention(0)],
                          [self.nearest.findAllPointsWith(i, 2).getDimention(1)],
                          styles[i])
            '''
            '''
            self.ax1.plot([self.dataPoints.points[i][0], self.nearest.points[i][0]],
                          [self.dataPoints.points[i][1], self.nearest.points[i][1]], style + '-')
            '''

            # Plotar todos os centroides
            self.ax1.plot(self.centroids.points[i][0], self.centroids.points[i][1], self.colors[i%len(self.colors)] + 's')

    
        
    def show(self):
        # Mostrar gráfico
        figManager = plt.get_current_fig_manager()
        figManager.full_screen_toggle()
        plt.show()
        
    def close(self):
        # Destruir gráfico
        plt.close()
