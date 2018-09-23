# -*- coding: utf-8 -*-


passwdList = []
valid = False
count = 3
while count > 0:
    input = raw_input("enter password")
    # check for valid passwd
    for eachPasswd in passwdList:
        if input == eachPasswd:
            valid = True
            break

    if not valid:
        print "invalid input"
        count -= 1
        continue
    else:
        break



