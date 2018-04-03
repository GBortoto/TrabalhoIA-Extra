import matplotlib.pyplot as plt
import matplotlib.animation as animation
#from matplotlib import style
from ListOfPoints import ListOfPoints
import time
import _thread
import sys
import random

class HarryPlotter():
    def __init__(self):
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1, 1, 1)
        #style.use('fivethirtyeight')
        self.data = ListOfPoints(10, 2, 100)
        self.data.points = [[i, i+1] for i in range(10)]
        self.ani = animation.FuncAnimation(self.fig, self.animate, interval=500)

    def animate(self, i):
        self.ax1.clear()
        self.ax1.plot(self.data.getDimention(0), self.data.getDimention(1),'k.')

    def run(self):
        plt.show()
        
    def stop(self):
        plt.close()
