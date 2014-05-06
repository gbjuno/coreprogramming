#!/usr/bin/env python

#from decimal import Decimal

def sort(userArray):
    userArray.sort()
    userArray.reverse()
    return

def main():
    userArray = []
    while True:
        try:
            userInput = raw_input("input numbers : ")
            userArray.append(userInput)
        except EOFError:
            print "ok,the array is %s" % repr(userArray)
            sort(userArray)
            print "after sort function, the array is %s" % repr(userArray)
            exit(0)
        except Exception as e:
            print e
            print "Input invalid!!!"
            exit(1)

if __name__ == '__main__':
    main()
