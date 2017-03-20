import requests
import bs4
import collections

weatherReport = collections.namedtuple('WeatherReport',
                                       'loc, cond, temp, scale')


def main():
    printHeader()
    userLoc = input("What zipcode should I look up (e.g. 90210)?: ")

    weatherHTML = fetchWeather(userLoc)

    weatherDeets = parseHTML(weatherHTML)

    print("The temperature for {} is {}{} and {} skies.".format(
        weatherDeets.loc,
        weatherDeets.temp,
        weatherDeets.scale,
        weatherDeets.cond
    ))


def printHeader():
    print("---------------------------------")
    print("       Real Time Weather")
    print("---------------------------------")
    print()


def fetchWeather(locale):
    url = "https://www.wunderground.com/weather-forecast/{}".format(locale)
    fetchResp = requests.get(url)
    return fetchResp


def parseHTML(rawHTML):
    """
    This method receives raw HTML, then extracts and returns wanted info.

    :param rawHTML: raw HTML from wuderground URL with appended user location.
    :return: A tuple with items (location, condition, temperature, temp scale).
    """
    soup = bs4.BeautifulSoup(rawHTML.text, 'lxml')

    '''
    cityCSS = 'div#location h1'
    weatherConditionCSS = 'div#curCond span.wx-value'
    weatherTempCSS = 'div#curTemp span.wx-data span.wx-value'
    weatherScaleCSS = 'div#curTemp span.wx-data span.wx-unit'
    '''

    location = extractCity(cleanText(soup.find(id='location').find('h1').get_text()))
    condition = cleanText(soup.find(id='curCond').find(class_='wx-value').get_text())
    temp = cleanText(soup.find(id='curTemp').find(class_='wx-data').find(class_='wx-value').get_text())
    tempScale = cleanText(soup.find(id='curTemp').find(class_='wx-data').find(class_='wx-unit').get_text())

    report = weatherReport(loc=location, cond=condition, temp=temp, scale=tempScale)
    return report


def cleanText(dirty : str):
    if not dirty:
        return dirty

    cleaned = dirty.strip()
    return cleaned


def extractCity(cleanLoc : str):
    cityPart = cleanLoc.split('\n')
    return cityPart[0].strip()

if __name__ == '__main__':
    main()



