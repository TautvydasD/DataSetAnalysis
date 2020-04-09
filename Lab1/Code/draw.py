import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import seaborn as sn
from numpy import log as ln
from Code.continues import Con
from Code.categoric import Categoric

def sepheaders(data):
    headers = data.columns   
    cont = []
    categ = []
    for header in headers:
        if data[header].dtype == np.float64:
            cont.append(header)
        else:
            categ.append(header)
    return cont, categ

def drawhistogram(data):
    cont, categ = sepheaders(data)
    for header in cont:
        plt.figure(num=header)
        binvalue =int(1 + 3.22 * ln(len(data[header])))
        data[header].hist(bins=binvalue)
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.title(header+" histogram")
    plt.show()

def drawbarplot(data, header):
    data[header].plot.bar(rot=0)

def drawbarplotcategoric(data):
    cont, categ = sepheaders(data)
    for header in categ:
        plt.figure(num=header)
        data[header].value_counts().plot(kind='bar')
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.title(header+" histogram")
    plt.show()

def drawscatter(data, header, header1):
    plt.figure(num=header+header1)
    plt.scatter(data[header], data[header1])
    plt.xlabel(header)
    plt.ylabel(header1)
    plt.show()

def splom(data):
    cont, categ = sepheaders(data)
    pd.plotting.scatter_matrix(data, alpha=0.2)
    plt.show()

def drawboxplot(data, header):
    df = pd.DataFrame()

    # data[header].plot.box()
    # data[header].plot.box(grid='True')
    # plt.show()


def drawcorrelation(data):
    corrMatrix = data.corr()
    sn.heatmap(corrMatrix, annot=True)
    plt.show()