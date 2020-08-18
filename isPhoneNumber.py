#!/usr/bin/env python3

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))
print(isPhoneNumber('1234-123-1245'))
print(isPhoneNumber('555-123-4567'))

#The same program above using regex

import re

print('==' * 30)
print('**' * 30)
print('==' * 30)

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
newphoneNumber = re.compile(r'\d\d\d-\d\d\d\-\d\d\d\d')
mo = newphoneNumber.search(message)
print(mo.group())

# Another way to print all occurrences

print('Another way to print all occurrences')
print('==' * 30)
print('**' * 30)
print('==' * 30)

newphoneNumberRegex = re.compile(r'\d\d\d-\d\d\d\-\d\d\d\d')
print(newphoneNumberRegex.findall('Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'))

      
print('==' * 30)
print('**' * 30)
print('==' * 30)

#####################################

print('**' * 25)
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    #print(chunk)
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done.')        


#Using Regexes
import re

print('**' * 30)
print('**' * 30)
print('**' * 30)
print('Time to use Regexes')

phoneNumberRegex =re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('My number is 512-584-9702')
print('Number found: ' + mo.group())

