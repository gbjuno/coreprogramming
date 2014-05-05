#!/usr/bin/env python

def transToEng(number):
    numEng = ('zero','one','two','three','four','five','six','seven','eight','nine')
    numArray =  list(str(number))
    for i in numArray:
        print "%s " % numEng[int(i)],

def main():
    userInput = raw_input("input number : ")
    try:
        transToEng(int(userInput))
    except Exception as e:
        print e
        print "Input is not a valid Integer"

if __name__ == '__main__':
    main()
