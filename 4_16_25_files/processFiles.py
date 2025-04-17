#

def readFile(fileName):
    openFile = open(fileName, "r")
    fileContent = openFile.readlines()
    openFile.close()

    return fileContent

def writeFile(fileName, input):
    openFile = open(fileName, "w")
    openFile.write(str(input))
    openFile.close()