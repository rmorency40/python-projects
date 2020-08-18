#!/usr/bin/env python3

import re
namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.findall('Agent Alice gave the  secret documents to Agent Bob.')
print(mo)

print('substitution ' * 5)
print()
mo1 = namesRegex.sub('REDACTED', 'Agent Alice gave the  secret documents to Agent Bob.')
print(mo1)

# print out the first letter by using group

print('The first letter')
print()
print()
namesRegex = re.compile(r'Agent (\w)\w*')
mo2 = namesRegex.findall('Agent Alice gave the  secret documents to Agent Bob.')
print(mo2)

print()
print()
mo3 = namesRegex.sub(r'Agent \1****', 'Agent Alice gave the  secret documents to Agent Bob.')
print(mo3)

print()
print('Using VERBOSE Mode ' * 3)
print()

re.compile(r'''
(\d\d\d-) |   # are code(without parens, with dash)
(\(\d\d\d\) )  # or area code with parens and no dash
\d\d\d        # first 3 digits
-             #second dash
\d\d\d\d      # last 4 digits
\sx\d{2,4}     # extension, like x1234''', re.VERBOSE | re.IGNORECASE | re.DOTALL)



