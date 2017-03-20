import os


def main():
    printHeader()

    directory = getDirectoryFromUser()
    if not directory:
        print("Sorry, cannot search that location.")
        return

    searchText = getSearchTextFromUser()
    if not searchText:
        print("Cannot search for nothing!")
        return

    matches = searchNow(directory, searchText)

    for m in matches:
        print(m)


def printHeader():
    print("---------------------------------")
    print("      File Search Utility")
    print("---------------------------------")
    print()


def getDirectoryFromUser():
    directory = input("What directory do you want to search?")
    if not directory or not directory.strip():
        return None

    if not os.path.isdir(directory):
        return None

    return os.path.abspath(directory)


def getSearchTextFromUser():
    txt = input("Search for what [single phrase only]?")

    return txt.lower()


def searchNow(directory, txt):

    allMatches = []

    items = os.listdir(directory)

    for item in items:
        fullItem = os.path.join(directory, item)
        if os.path.isdir(fullItem):
            continue

        matches = searchFile(fullItem, txt)
        allMatches.extend(matches)

    return allMatches


def searchFile(fileName, searchTxt):
    matches = []
    with open(fileName, 'r', encoding='utf-8',) as fin:

        for line in fin:
            if line.lower().find(searchTxt) >= 0:
                matches.append(line)

        return matches


if __name__ == '__main__':
    main()
