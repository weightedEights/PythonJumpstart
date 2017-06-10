import csv
import os

from dataTypes import Purchase

def main():

    printHeader()
    datFile = getDataFile()
    loadedData = loadData(datFile)
    queryData(loadedData)


def printHeader():
    print("---------------------------------")
    print("      Real Estate Analysis")
    print("---------------------------------")
    print()


def getDataFile():
    baseFolder = os.path.dirname(__file__)
    return os.path.join(baseFolder, 'data', 'SacramentoRealEstateTransactions2008.csv')


def loadData(datFile):
    with open(datFile, 'r', encoding='utf-8') as fin:
        return [Purchase.createFromDict(row) for row in csv.DictReader(fin)]


def queryData(loadedData):

    loadedData.sort(key=lambda p: p.price)

    high_purchase = loadedData[-1]
    print("The most expensive house is ${:,} with {} beds and {} baths.".format(
        high_purchase.price, high_purchase.beds, high_purchase.baths))

    low_purchase = loadedData[0]
    print("The least expensive house is ${:,} with {} beds and {} baths.".format(
        low_purchase.price, low_purchase.beds, low_purchase.baths))

    return loadedData


if __name__ == '__main__':
    main()