#!/usr/bin/env python

def stockDataSort(stockData,userInput):
    stockDataAfterSort = {}
    if userInput == None:
        print "input wrong items"
        exit(1)
    else:
        for i in stockData:
            stockDataAfterSort[i[userInput]] = i
    print "-----------------------------------"
    for dataItem in sorted(stockDataAfterSort):
        print "%s : %s" % (dataItem,stockDataAfterSort[dataItem])
    print "-----------------------------------"
    return stockDataAfterSort
        
def main():
    stockData = [
        ['1000',1.6,1.7,1000],
        ['3023',101.5,0,0],
        ['0032',300.1,298,300],
        ['2032',30.2,40,60000]
    ]
    userInputMap = {"number":0,"currentPrice":1,"buyPrice":2,"stockNumber":3}
    
    userInput = "number"
    print "stockDataAfterSort is %s " % stockDataSort(stockData,userInputMap.get(userInput))

    userInput = "currentPrice"
    print "stockDataAfterSort is %s " % stockDataSort(stockData,userInputMap.get(userInput))
    
    userInput = "buyPrice"
    print "stockDataAfterSort is %s " % stockDataSort(stockData,userInputMap.get(userInput))
    
    userInput = "stockNumber"
    print "stockDataAfterSort is %s " % stockDataSort(stockData,userInputMap.get(userInput))

    userInput = "haha"
    print "stockDataAfterSort is %s " % stockDataSort(stockData,userInputMap.get(userInput))
    
if __name__ == '__main__':
    main()
