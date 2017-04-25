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
        yield [Purchase.createFromDict(row) for row in csv.DictReader(fin)]


def queryData(loadedData):
    return loadedData


if __name__ == '__main__':
    main()