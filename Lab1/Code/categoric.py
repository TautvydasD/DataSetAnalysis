import numpy as np
import math
import pandas as pd

class Categoric:
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
        return [val for val in self.datalist if val is not np.nan]

    def length(self):
        return len(self.dataframe)

    def missingpercent(self):
        return sum( 1 for val in self.dataframe if val is np.nan) / self.length() * 100
    
    def cardinality(self):     
        return len(set(self.clearlist()))

    def valueoccurences(self):
        alldata = self.clearlist()
        dictionary = {val:alldata.count(val) for val in set(self.clearlist())}
        return {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1])}
    
    def mode(self):
        return list(self.valueoccurences().keys())[-1]
    
    def modecount(self):
        return list(self.valueoccurences().values())[-1]

    def modepercentage(self):
        return self.modecount() / self.length() * 100

    def mode2(self):
        return list(self.valueoccurences().keys())[-2]
    
    def mode2count(self):
        return list(self.valueoccurences().values())[-2]

    def mode2percentage(self):
        return self.mode2count() / self.length() * 100