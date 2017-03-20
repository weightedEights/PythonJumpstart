import os


def load(name):
    """
    This method creates and loads a new journal.

    :param name: Base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    """
    data = []
    filename = getFullPath(name)
    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journalData):
    filename = getFullPath(name)
    print("Saving to: {}".format(filename))

    with open(filename, 'w') as fout:
        for entry in journalData:
            fout.write(entry + '\n')


def getFullPath(name):
    return os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))


def addEntry(txtBody, journalName):
    journalName.append(txtBody)