from HarryPlotter import HarryPlotter as HP
from ListOfPoints import ListOfPoints
from random import random
import time
import sys
import _thread

data = ListOfPoints(10, 2, 100)

for i in range(10):
    data.points[i] = [random() * 100, random() * 100]


def executeCode(a, b):
    for i in range(10, 100):
        time.sleep(0.5)
        data.points.append([random() * 100, random() * 100])

def hidePlotterOnDemand(plotter, b):
    text = ""
    while(text.lower() != 'p'):
        text = input("Para parar, digite p\n")
    plotter.close()


def test():
    plotter = HP(data, 1000)
    
    try:
        _thread.start_new_thread(executeCode, (0, 0))
        _thread.start_new_thread(hidePlotter, (plotter, 0))
        plotter.show()
        
    except Exception as e:
        print(e)
