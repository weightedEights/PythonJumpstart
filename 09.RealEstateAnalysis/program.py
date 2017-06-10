import csv
import os
import statistics

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

    # show average price for all homes
    purchase_prices = [purchase.price for purchase in loadedData]
    mean_purchase_price = statistics.mean(purchase_prices)

    print("The average home price is ${:,}.".format(int(mean_purchase_price)))

    # show stats for 2BR homes
    twoBR_stats = [purchase for purchase in loadedData if purchase.beds == 2]
    avg_price = statistics.mean(p.price for p in twoBR_stats)
    avg_baths = statistics.mean(p.baths for p in twoBR_stats)
    avg_sqft = statistics.mean(p.sq__ft for p in twoBR_stats)

    print("The average 2-bedroom home price is ${:,} with {} baths and {} sq ft.".format(
        int(avg_price), round(avg_baths, 1), round(avg_sqft, 1)))


    return loadedData


if __name__ == '__main__':
    main()