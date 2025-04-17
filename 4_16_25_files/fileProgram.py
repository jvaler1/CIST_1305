# 

from processFiles import *


def main():
    # myText = readFile("myFile1.txt")
    # print(myText)

    newFileName = input("New Text File Name: ") + ".txt"
    newFileInput = input("New File input: ")

    writeFile(newFileName, newFileInput)
    
    print(readFile(newFileName))
    
main()