import datetime
import journal


def main():
    printHeader()
    eventLoop()


def printHeader():
    print("---------------------------------")
    print("      Journal Keeper Lite")
    print("---------------------------------")
    print()


def eventLoop():
    print("What would you like to do?")

    cmd = "Empty"

    journalName = "default"
    journalData = journal.load(journalName) #[] #list()

    while cmd != 'x' and cmd:
        cmd = input("[L]ist entries. [A]dd new entry. E[x]it journal. : ")
        cmd = cmd.lower().strip()

        if cmd == 'l':
            listEntries(journalData)
        elif cmd == 'a':
            addEntry(journalData)
        elif cmd != 'x' and cmd:
            print("Sorry, I dont understand command '{}'.".format(cmd))
            print()

    print("Done. Goodbye.")
    journal.save(journalName, journalData)


def listEntries(data):
    print("Current entries: ")
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print("* [{}] {}".format(idx+1, entry))


def addEntry(data):
    txtBody = input("Type entry here, <enter> will exit: ")

    journal.addEntry(txtBody, data)

    # data.append(txtBody)

if __name__ == '__main__':
    main()

