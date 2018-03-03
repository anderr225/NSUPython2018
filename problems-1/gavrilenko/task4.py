import sys
import os


def printList(path):
    files = []

    for name in os.listdir(path):
        filePath = os.path.join(path, name)
        if os.path.isfile(filePath):
            files += [(name, os.stat(filePath).st_size)]

    files.sort(key=lambda x: x[0])
    files.sort(key=lambda x: x[1], reverse=True)

    for name, size in files:
        print(name, size)


def main():
    if len(sys.argv) != 2:
        print("Wrong number of arguments")
    else:
        printList(sys.argv[1])


main()
