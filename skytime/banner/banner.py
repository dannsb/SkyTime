from os import system

def printBanner():
    with open("banner/banner.txt", "r") as f:
        for line in f:
            print(line.rstrip())
