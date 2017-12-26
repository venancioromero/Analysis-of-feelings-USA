#!/usr/bin/env python
import json,sys, operator,math

countMessages = {}
scoreDict = {}
nameStates = {}


def addScore(key,value):
    if key in scoreDict:
        scoreDict[key] += value
        countMessages[key] += 1
    else:
        scoreDict[key] = value
        countMessages[key] = 1
        
def normalizeScore():
    for x in scoreDict:
        if countMessages[x] > 0:
            scoreDict[x] = scoreDict[x]*100/countMessages[x]

def printDict(dicti):
    for x in dicti:
        print '%s\t%s' % (x,dicti[x])

def main():
    for line in sys.stdin:
        key, value = line.strip().split('\t', 1)
        addScore(key,int(value))

    normalizeScore()
    printDict(scoreDict)

if __name__ == '__main__':
    main()
    

    