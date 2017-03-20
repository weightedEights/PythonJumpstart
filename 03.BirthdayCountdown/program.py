import datetime

def printHeader():
    print("---------------------------------")
    print("    Birthday Countdown Timer")
    print("---------------------------------")
    print()


def getBdayFromUser():
    print("When were you born?")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    bDay = datetime.datetime(year, month, day)
    return bDay


def calcDaysBetweenDates(userDate, nowDate):
    date2 = datetime.datetime(nowDate.year, userDate.month, userDate.day)
    dt = nowDate - date2
    days = int(dt.total_seconds() / 60 / 60 / 24)
    return days


def printBdayInfo(days):
    if days < 0:
        print("Your birthday is in {} days!".format(-days))
    elif days > 0:
        print("Your birthday has already passed this year, {} days ago.".format(days))
    else:
        print("Happy birthday!")


def main():
    printHeader()
    bDay = getBdayFromUser()
    nowDate = datetime.datetime.now()
    dayCount = calcDaysBetweenDates(bDay,nowDate)
    printBdayInfo(dayCount)


main()