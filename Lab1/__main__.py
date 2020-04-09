import numpy as np
import math
import seaborn as sn
from Code.continues import Con
from Code.categoric import Categoric
from Code import draw
from Code import inout

 # Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
def main():
    dat = inout.read("./Lab1/Data/Game_Data.csv")
    cont = Con(dat["Year_of_Release"])
    # print(dat["Year_of_Release"].describe())
    print(cont.thirdquarter())

    # results(dat)
    # drawhistogram(dat)
    # drawbarplotcategoric(dat)
    draw.drawscatter(dat, "Other_Sales", "NA_Sales")
    # splom(dat)
    # drawboxplot(dat,"Platform")
    # drawcorrelation(dat)

if __name__ == "__main__":
    main()
