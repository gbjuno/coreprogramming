#!/usr/bin/env python

from random import randint

def randset():
    returnSet = set()
    result = randint(0,9)
#    print "random set element number : %s" % result
    for i in range(result):
        result2 = randint(0,9)
        returnSet.add(result2)
#        print "randint is %s,therefore returnset = % s" % (result2,returnSet)
    return returnSet

def compare(userInput,result):
    userResultList = [ int(x) for x in userInput.split(',')]
    userResult = set([ int(x) for x in userInput.split(',')])
    print "userResult = %s " % str(userResult)
    if userResult == result:
        if len(userResult) == len(userResultList):
             return True
        else:
             print "you input the same element in your answer"
             return False
    else:
        return False


def main():
    A = randset()
    B = randset()
    print "A=%s,B=%s" % (A,B)
    count = 0
    while count < 3:
        try:
            userInput = raw_input("input your answer of A|B :")
            if compare(userInput,A|B):
                print "your answer is right"
                break
            else:
                print "wrong answer"
                count += 1
        except Exception as e:
            print e
            print "you input is invalid"
    print "A|B = %s" % str(A|B)
if __name__ == '__main__':
    main() 
