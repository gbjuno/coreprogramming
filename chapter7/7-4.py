#!/usr/bin/env python

def makeDict(list1,list2):
    if len(list1) == len(list2):
        myDict = dict(zip(list1,list2))
        print "the dict is %s" % myDict
        return myDict
    else:
        print "the two list is not the same long"
        exit(1)

def sortAndPrint(myDict):
    for i in sorted(myDict):
        print "%s:%s" % (i,myDict[i]),

def main():
    list1 = list('1234567')
    list2 = list('abcdefg')
    sortAndPrint(makeDict(list1,list2))

if __name__ == '__main__':
    main()

