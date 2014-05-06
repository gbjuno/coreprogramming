#!/usr/bin/env python

def reverse(myDict):
    revDict = {}
    for i in myDict:
        revDict[myDict[i]] = i
    return revDict 
        

def main():
    myDict = dict(zip(list('1234'),list('abcd')))
    print "myDict = %s" % myDict
    print "revDict = %s" % reverse(myDict)

if __name__ == '__main__':
    main()
