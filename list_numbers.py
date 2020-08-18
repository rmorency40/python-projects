#! /usr/bin/env python3

# generate list of numbers

import random, sys, os

#os.chmod('C:/Users/rmorency/AppData/Local/Programs/Python/Python37/Scripts/phone_numbers.csv', 777)
sys.stdout = open('phone_numbers02.csv', 'w+')
print("The first 10000 phone numbers")
for number in range(50900000000, 50999999999, 10000):
    print(number)

   
f = open('toto.txt', 'w')
for i in range(12):
    f.write("This is line %d\r\n" % (i+1))
    for n in range(15):
        f.write("This is the second range of rows %d\r\n" % (n+1))
f.close()    
