#!/usr/bin/env python

def alphaReverse(userInput):
    userInputList = list(userInput)
    userOutputList = []
    for i in userInput:
        if i.islower():
            userOutputList.append(i.upper())
        elif i.isupper():
            userOutputList.append(i.lower())
        else:
            userOutputList.append(i)
    return ''.join(userOutputList)
        

def main():
    userInput = raw_input("input the string : ")
    print "the reversed string is : %s " % alphaReverse(userInput)

if __name__ == '__main__':
    main()
