#!/usr/bin/env python

def singleBase(numToEngMap,numStr):
    return numToEngMap[numStr]

def tenBase(numToEngMap,numStr):
    if numToEngMap.has_key(numStr[-2:]):
        numToEng = "%s" % numToEngMap[numStr[-2:]]
    else:
        numToEng = "%s-%s" % (numToEngMap[numStr[-2]+'0'],numToEngMap[numStr[-1]])
    return numToEng

def hundredBase(numToEngMap,numStr):
    numToEng_ten = tenBase(numToEngMap,numStr)
    numToEng_hundred = numToEngMap[numStr[-3]]
    if numToEng_ten and numToEng_hundred != 'zero':
        numToEng = "%s hundred and %s" % (numToEng_hundred,numToEng_ten)
    elif numToEng_hundred != 'zero':
        numToEng = "%s hundred" % numToEng_hundred
    elif numToEng_ten:
        numToEng = "%s" % numToEng_ten
    else:
        numToEng = ''
    return numToEng

def thousandBase(numToEngMap,numStr):
    numToEng_hundred = hundredBase(numToEngMap,numStr)
    numToEng_thousand = numToEngMap[numStr[-4]]
    if numToEng_hundred:
        numToEng = "%s thousand and %s" % (numToEng_thousand,numToEng_hundred)
    else:
        numToEng = "%s thousand" % numToEng_thousand
    return numToEng

def transToEng(number):
    numToEngMap = {'0':'zero','00':'',
                   '1':'one','01':'one',
                   '2':'two','02':'two',
                   '3':'three','03':'three',
                   '4':'four','04':'four',
                   '5':'five','05':'five',
                   '6':'six','06':'six',
                   '7':'seven','07':'seven',
                   '8':'eight','08':'eight',
                   '9':'nine','09':'nine',
                   '10':'ten',
                   '11':'eleven',
                   '12':'twelve',
                   '13':'thirteen',
                   '14':'fourteen',
                   '15':'fifteen',
                   '16':'sixteen',
                   '17':'seventeen',
                   '18':'eighteen',
                   '19':'nineteen',
                   '20':'twenty',
                   '30':'thirty',
                   '40':'forty',
                   '50':'fifty',
                   '60':'sixty',
                   '70':'seventy',
                   '80':'eighty',
                   '90':'ninty'}
    numStr = str(number)
    if len(numStr) == 1:
        numToEng = singleBase(numToEngMap,numStr)
    elif len(numStr) == 2:
        numToEng = tenBase(numToEngMap,numStr)
    elif len(numStr) == 3:
        numToEng = hundredBase(numToEngMap,numStr)
    elif len(numStr) == 4:
        numToEng = thousandBase(numToEngMap,numStr) 
    print "the number in English : %s " % numToEng
    return

def main():
    userInput = raw_input("input number : ")
    try:
        transToEng(int(userInput))
    except Exception as e:
        print e
        print "Input is not a valid Integer"

if __name__ == '__main__':
    main()
