import os
import platform
import subprocess
import catService


def main():
    printHeader()
    folder = getOrCreateFolder()
    print("Found or created folder " + folder)
    downloadCats(folder)
    displayCats(folder)


def printHeader():
    print("---------------------------------")
    print("        LOL Cat Factory")
    print("---------------------------------")
    print()


def getOrCreateFolder():
    baseDir = os.path.dirname(__file__)
    print(baseDir)
    folder = 'catPics'
    fullPath = os.path.join(baseDir, folder)

    if not os.path.exists(fullPath) or not os.path.isdir(fullPath):
        print("Creating new directory {}..".format(fullPath))
        os.mkdir(fullPath)

    return fullPath


def downloadCats(folder):
    print("Contacting download server..")
    catCount = 8
    for i in range(1, catCount+1):
        # print(i, end=', ')
        name = "lolcat_{}".format(i)
        print("Downloading {}..".format(name))
        catService.getCat(folder, name)
    print("Download complete.")


def displayCats(folder):
    # open folder
    print("Displaying cats in OS window.")
    if platform.system() == "Darwin":
        subprocess.call(['open', folder])
    elif platform.system() == "Linux":
        subprocess.call(['xdg-open', folder])
    elif platform.system() == "Windows":
        print(folder)
        subprocess.call(['explorer', folder])
    else:
        print("OS {} not supported".format(platform.system()))


if __name__ == '__main__':
    main()
