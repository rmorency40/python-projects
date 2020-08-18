#!/usr/bin/env python3

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d\-\d\d\d\d')
mo = phoneNumRegex.search('My number is 407-111-1111')
print(mo.group())

print('==' * 30)
print('==' * 30)

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d\-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 407-111-1111')
print(mo.group(1))

# Looking for parentheses in the string

print('==' * 30)
print('**' * 30)

phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d\-\d\d\d\d')
mo = phoneNumRegex.search('My number is : (407) 111-1111')
print(mo.group())

print('**' * 30)
print('==' * 30)

# Regex with pipe

print('**' * 30 + 'pipe')
print('==' * 30 + 'pipe')

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group(1))
print(mo.group())
