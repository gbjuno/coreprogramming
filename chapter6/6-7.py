#!/usr/bin/env python

#get the user input
num_str = raw_input('Enter a number: ')

#transfer user input into type int
num_num = int(num_str)

#get the number from 1 to num+1 list
fac_list = range(1, num_num+1)
print "BEFORE:", `fac_list`

#
i = 0
userList = []
while i < len(fac_list):
    if num_num % fac_list[i] == 0:
        userList.append(fac_list.pop(i))
    else:
        i = i + 1

print "AFTER:", `fac_list`
print "List:", `userList`
