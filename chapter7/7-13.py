#!/usr/bin/env python

from random import randint

def randset():
    returnSet = set()
    result = randint(0,9)
    print "random set element number : %s" % result
    for i in range(result):
        result2 = randint(0,9)
        returnSet.add(result2)
        print "randint is %s,therefore returnset = % s" % (result2,returnSet)
    return returnSet
        

def main():
    A = randset()
    B = randset()
    print "A=%s,B=%s" % (A,B)
    print "A|B = %s" % str(A|B)
    print "A&B = %s" % str(A&B)

if __name__ == '__main__':
    main() 
