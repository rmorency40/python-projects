#!/usr/bin/python

string = input("enter your own string : ")
char = input("Enter your own character: ")
flag = 0
#if not string:
#    print("this is not a string")
for i in range(len(string)):
        if (string[i] == char):
            flag = 1
            break
if (flag == 0):
    print("Sorry, we haven't found the search character in this string")
else:
    print("The first occurence of", char, "is found at position", i + 1)
