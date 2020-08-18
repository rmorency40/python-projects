#!/usr/bin/python v3

#Python Program - Display Caeender

import calendar
print ("---------- Calendar Program in Python --------\n");
print("Enter 'x'x for exit.");
y = input("Enter year: ");
if y == 'x':
    exit();
else:
    m = input("Enter month: ");
    yy = int(y);
    mm = int(m);
    print("\n",calendar.month(yy,mm));
    

