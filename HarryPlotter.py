import matplotlib.pyplot as plt
import matplotlib.animation as animation
#from matplotlib import style
from ListOfPoints import ListOfPoints
import time
import _thread
import sys
import random

class HarryPlotter():
    def __init__(self, dataPoints:ListOfPoints, centroids:ListOfPoints, nearest:ListOfPoints, refreshRate:int=1000):
        """Recebe um ListOfPoints e cria um gráfico dinâmico"""
        # Cria ambiente onde o plot acontecerá
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1, 1, 1)

        # Cria uma referência aos ListOfPoints
        self.dataPoints = dataPoints
        self.centroids = centroids
        self.nearest = nearest

        self.firstPlot = 5
        #print(dataPoints)
        #print(centroids)
        #print(nearest)

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
        else:

            group0 = []
            group1 = []
            group2 = []
            group3 = []
            
            # Plotar todos os pontos em dataPoints
            for i in range(len(self.dataPoints)):
                style = 'k'
                if(self.nearest.points[i][2] == 0):
                    style = 'r'
                    group0.append([self.dataPoints.points[i][0], self.dataPoints.points[i][1]])
                elif(self.nearest.points[i][2] == 1):
                    style = 'g'
                    group1.append([self.dataPoints.points[i][0], self.dataPoints.points[i][1]])
                elif(self.nearest.points[i][2] == 2):
                    style = 'b'
                    group2.append([self.dataPoints.points[i][0], self.dataPoints.points[i][1]])
                elif(self.nearest.points[i][2] == 3):
                    style = 'y'
                    group3.append([self.dataPoints.points[i][0], self.dataPoints.points[i][1]])

            self.ax1.plot([group0[i][0] for i in range(len(group0))],
                          [group0[i][1] for i in range(len(group0))],
                          'ro')
            self.ax1.plot([group1[i][0] for i in range(len(group1))],
                          [group1[i][1] for i in range(len(group1))],
                          'go')
            self.ax1.plot([group2[i][0] for i in range(len(group2))],
                          [group2[i][1] for i in range(len(group2))],
                          'bo')
            
            self.ax1.plot([group3[i][0] for i in range(len(group3))],
                          [group3[i][1] for i in range(len(group3))],
                          'yo')
            
            
            styles = ['r-', 'g-', 'b-', 'y-']
            for i in range(4):
                #print(i)
                indexes_pointsInCluster = self.nearest.findAllPointsWith(i, 2).getDimention(3)
            
                pointsInCluster = ListOfPoints(len(indexes_pointsInCluster), 2, 100)

                for j in range(len(pointsInCluster)):
                    pointsInCluster.points[j] = self.dataPoints.points[indexes_pointsInCluster[j]]

                xType1 = pointsInCluster.getDimention(0)
                xType2 = self.nearest.findAllPointsWith(i, 2).getDimention(0)
                yType1 = pointsInCluster.getDimention(1)
                yType2 = self.nearest.findAllPointsWith(i, 2).getDimention(1)

                drawLines = []
                #print('xType1')
                #print(xType1)
                #print('yType1')
                #print(yType1)
                #print('xType2')
                #print(xType2)
                #print('yType2')
                #print(yType2)

                for j in range(len(pointsInCluster)):
                    self.ax1.plot([xType1[j], xType2[j]],
                                  [yType1[j], yType2[j]],
                                  styles[i])
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
            self.ax1.plot(self.centroids.points[0][0], self.centroids.points[0][1], 'rs')
            self.ax1.plot(self.centroids.points[1][0], self.centroids.points[1][1], 'gs')
            self.ax1.plot(self.centroids.points[2][0], self.centroids.points[2][1], 'bs')
            self.ax1.plot(self.centroids.points[3][0], self.centroids.points[3][1], 'ys')

    
        
    def show(self):
        # Mostrar gráfico
        figManager = plt.get_current_fig_manager()
        figManager.full_screen_toggle()
        plt.show()
        
    def close(self):
        # Destruir gráfico
        plt.close()
