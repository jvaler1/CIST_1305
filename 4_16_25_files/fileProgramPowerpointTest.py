#

from processFiles import *

def main():

    num1 = int(input("Enter a number: "))
    writeFile("num1File",num1)
    print('num1File.txt')

main()