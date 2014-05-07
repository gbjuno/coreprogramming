#!/usr/bin/env python

def isLeap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def calDates(someDate):
    daysMap = [31,28,31,30,31,30,31,31,30,31,30,31]
    someDateList = someDate.split('/')
    countdays = int(someDateList[0])
#    print "at first countdays is %s" % countdays
    for i in range(int(someDateList[1])-1):
#        print "%s, countdays = %s + %s " % (i,countdays,daysMap[i])
        countdays += daysMap[i]
    if int(someDateList[1]) > 2 and isLeap(int(someDateList[2])):
#        print "leap year,therefore countdays = %s + 1" % countdays
        countdays += 1
#        print "now countdays is %s" % countdays
    for i in range(1,int(someDateList[2])):
        if isLeap(i):
#            print "%s is leap year,countdays = %s + 366" % (i,countdays)
            countdays += 366
#            print "now countdays is %s" % countdays
        else:
#            print "%s is not leap year,countdays = %s + 365" % (i,countdays)
            countdays += 365
#            print "now countdays is %s" % countdays
    return countdays

def main():
#    date1 = raw_input("input date1 in form DD/MM/YYYY: ")
#    date2 = raw_input("input date2 in form DD/MM/YYYY: ")
    date1 = '1/4/1999'
    date2 = '1/3/2000'
    print "date 1 is %s, date 2 is %s, date 1 minus date 2 is %s days "% (date1,date2,calDates(date1)-calDates(date2))
    print "date 1 is %s, date 2 is %s" % (calDates(date1),calDates(date2))
#    date1 = '1/1/2012'
#    print "----------calculate %s start----------" % date1
#    result = calDates(date1)
#    print "----------calculate %s  end ----------" % date1
#    print "finally countdays is %s " % result

if __name__ == '__main__':
    main()
