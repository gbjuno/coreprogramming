#!/usr/bin/env python

def intToIP():
    userInputInt = raw_input("Input integer : ")
    if len(userInputInt) <= 12:
        userInputInt = '0'*(12-len(userInputInt)) + userInputInt
        print "IP: %s:%s:%s:%s" % (userInputInt[:3],userInputInt[3:6],userInputInt[6:9],userInputInt[9:])
        exit(0)
    else:
        print "input is invalid"
 
def ipToInt():
    userInputIp = raw_input("input ip in this form WWW.XXX.YYY.ZZZ :")
    userOutInt = int(''.join(userInputIp.split('.')))
    print "INT: %s" % userOutInt
    exit(0)

def main():
    print """Options:
    (A)intToIP
    (B)ipToInt
    """
    while True:
        try:
            userInput = raw_input("INPUT YOUR CHOICE :")
            if userInput == 'A':
                intToIP()
            elif userInput == 'B':
                ipToInt()
            else:
                print "input again"
        except EOFError:
            print "exit ok\n"
            break
        except Exception as e:
            print e
            print "input your choice again,pleas"

if __name__ == '__main__':
    main()
