#!/usr/bin/env python

def myTrans(srcstr,dststr,myString,ignoreCase):
    goalStringList = []
    transTable = {}
    if not ignoreCase:
        for i in range(0,len(srcstr)):
             if (len(dststr)-1) >= i:
                 transTable.setdefault(srcstr[i],dststr[i])
                 transTable.setdefault(srcstr[i].upper(),dststr[i].upper())
             else:
                 transTable.setdefault(srcstr[i],'')
    print "transTable % s " % transTable
    for i in myString:
        goalStringList.append(transTable.get(i,i))
    return ''.join(goalStringList)

def main():
    srcstr = 'abc'
    dststr = 'xyz'
    ignoreCase = False
    myString = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print "translate %s to %s" % (myString,myTrans(srcstr,dststr,myString,ignoreCase))

if __name__ == '__main__':
    main()
