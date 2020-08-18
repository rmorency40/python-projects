#!/usr/bin/python3

# Extract email-id from URL text file

# library that handles the URL stuff

import urllib.request


# Importing module required for 
# regular expressions

import re


email_file = open('C:\\Users\\rmorency\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\e-mail-1.txt')


#for line in email_file:
    #if re.match(r'[\w\.-]+@[\w\.-]+', line):
        #print(line)
    
for email in email_file:
    if re.match(r'[A-Za-z0-1._%+-]+'
                r'@[A-Za-z0-9._]+', email):
                #r'\.[A-Za-z]{2, 4}', email):
        print(email)
    
    
