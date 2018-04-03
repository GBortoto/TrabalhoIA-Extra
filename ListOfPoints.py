class ListOfPoints():
    def __init__(self, size, dimentions, maxRange):
        self.points = [[0.0 for j in range(dimentions)] for i in range(size)]
        self.maxRange = maxRange

    def getNumberOfPoints(self):
        return len(self.points)

    def getDimentionOfPoints(self):
        return len(self.points[0])

    def getDimention(self, dimention):
        return [self.points[i][dimention] for i in range(self.getNumberOfPoints())]
        
    def plotPoints(self, mode, dimentionX=0, dimentionY=1):
        plt.plot(self.getDimention(dimentionX), self.getDimention(dimentionY), mode)

    def __str__(self):
        return str(self.points)

    __len__ = getNumberOfPoints
    __repr__ = __str__
