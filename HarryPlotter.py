import matplotlib.pyplot as plt
import matplotlib.animation as animation
#from matplotlib import style
from ListOfPoints import ListOfPoints
import time
import _thread
import sys
import random

class HarryPlotter():
    def __init__(self, data:ListOfPoints, centroids:ListOfPoints, clusters:ListOfPoints, refreshRate:int=1000):
        """Recebe um ListOfPoints e cria um gráfico dinâmico"""
        # Cria ambiente onde o plot acontecerá
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1, 1, 1)

        # Cria uma referência aos ListOfPoints
        self.data = data
        self.centroids = centroids
        self.clusters = clusters
        print(data)
        print(centroids)
        print(clusters)

        # Seta uma função de animação ao ambiente atual que atualiza a cada "refreshRate" milésimos
        self.ani = animation.FuncAnimation(self.fig, self.animate, refreshRate)

    def animate(self, i):
        """Função que é executada a cada iteração da animação, conforme o refreshRate"""
        # Limpar gráfico
        self.ax1.clear()

        #print(self.data)
        
        # Plotar todos os pontos em data
        for i in range(len(self.data)):
            
            style = 'k.'
            if(self.clusters.points[i] == 0):
                style = 'r.'
            elif(self.clusters.points[i] == 1):
                style = 'g.'
            elif(self.clusters.points[i] == 2):
                style = 'b.'
            elif(self.clusters.points[i] == 3):
                style = 'm.'

            self.ax1.plot(self.data.points[i][0], self.data.points[i][1], style)
        '''
            
        '''
        # Plotar todos os centroides
        self.ax1.plot(self.centroids.points[0][0], self.centroids.points[0][1], 'rs')
        self.ax1.plot(self.centroids.points[1][0], self.centroids.points[1][1], 'gs')
        self.ax1.plot(self.centroids.points[2][0], self.centroids.points[2][1], 'bs')
        self.ax1.plot(self.centroids.points[3][0], self.centroids.points[3][1], 'ms')
        
    def show(self):
        # Mostrar gráfico
        plt.show()
        
    def close(self):
        # Destruir gráfico
        plt.close()
