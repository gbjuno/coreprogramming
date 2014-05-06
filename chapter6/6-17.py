#!/usr/bin/env python

def myPop(myList):
    if len(myList) == 0:
         print "no more element to pop"
         exit(1)
    else:
         result = myList[len(myList)-1]
         myList.remove(result)
         return result

def myPush(myList,element):
    myList.append(element)

def main():
    myList = []
    for i in range(800,810,3):
        myPush(myList,i)
        print "myList push %s" % i
        print "myList = %s" % myList
    print "myList = %s" % myList
    for i in range(4):
        print "myList pop %s " % myPop(myList)
        print "myList = %s" % myList

if __name__ == '__main__':
    main()
