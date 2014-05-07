#!/usr/bin/env python

import random

def Rochambeau(userInput):
    strMap = {'1':'scissor','2':'rock','3':'paper'}
    computeInput = str(random.randint(1,3))
    result = str(int(computeInput) - int(userInput))
    resultMap = {'0':'yawk','-1':'win','-2':'lose','1':'lose','2':'win'}
    print "your input is %s" % strMap[userInput]
    print "computeInput is %s" % strMap[computeInput]
    print "you %s" % resultMap[result]


def main():
    print """
    1:scissor
    2:rock
    3:paper
    """
    userInput = raw_input("input your choice (1-3): ")
    Rochambeau(userInput)

if __name__ == '__main__':
    main()
