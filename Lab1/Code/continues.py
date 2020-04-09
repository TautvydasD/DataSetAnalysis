import numpy as np
import math
import pandas as pd

class Con:
    def __init__(self, dataframe):
        self.__dataframe = dataframe
        self.__datalist = dataframe.values.tolist()

    @property
    def dataframe(self):
        return self.__dataframe

    @property
    def datalist(self):
        return self.__datalist

    def clearlist(self):
        return sorted([val for val in self.dataframe if not np.isnan(val)])

    def length(self):
        return len(self.dataframe)

    def missingpercent(self):
        return sum(np.isnan(val) for val in self.dataframe) / self.length() * 100
    
    def cardinality(self):     
        return len(set(self.clearlist()))

    def max(self):
        return max(self.clearlist())

    def min(self):
        return min(self.clearlist())

    def firstquarter(self):
        index = len(self.clearlist()) % 4
        quarter = int(len(self.clearlist()) / 4)  
        if index == 0 or index == 1:
            return (self.clearlist()[quarter] + self.clearlist()[quarter - 1]) / 2 
        elif index == 2 or index == 3:
            return self.clearlist()[quarter]

    def thirdquarter(self):
        index = len(self.clearlist()) * 3 % 4
        quarter = int(len(self.clearlist()) * 3 / 4)
        if index == 0:
            return (self.clearlist()[quarter] + self.clearlist()[quarter -1]) / 2
        elif index == 3:
            return (self.clearlist()[quarter] + self.clearlist()[quarter + 1]) / 2
        elif index == 2 or index == 1:
            return self.clearlist()[quarter]

    def avg(self):
        return sum(self.clearlist()) / len(self.clearlist())

    def median(self):
        index = len(self.clearlist()) % 2
        middle = int(len(self.clearlist()) / 2)
        return self.clearlist()[middle] if index == 0 else (self.clearlist()[middle] + self.clearlist()[middle + 1]) / 2

    def variance(self):
        avg = int(self.avg()) 
        return sum([(val - avg) ** 2 for val in self.clearlist()]) / len(self.clearlist())

    def standartdev(self):
        return math.sqrt(self.variance())