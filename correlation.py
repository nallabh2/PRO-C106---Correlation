import csv
import plotly.express as px
import numpy as np

def getDataSource(dataPath):
    temperature=[]
    iceCreamSales=[]
    with open(dataPath) as f:
        csvReader=csv.DictReader(f)
        for item in csvReader:
            temperature.append(float(item["Temperature"]))
            iceCreamSales.append(float(item["Ice-cream Sales"]))
    return {"x":iceCreamSales,"y":temperature}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print(correlation)
    
def plotFigure(dataPath):
    with open(dataPath) as f:
        df=csv.DictReader(f)
        fig=px.scatter(df,x="Temperature",y="Ice-cream Sales")
        fig.show()

dataPath="Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
dataSource=getDataSource(dataPath)
findCorrelation(dataSource)
plotFigure(dataPath)

