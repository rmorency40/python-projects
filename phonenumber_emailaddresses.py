#! /usr/bin/env python3

# phoneAndEmail.py
# Finds phone numbers and email addresses on the clipboard.


import pyperclip, re
# Create a regex for phone numbers

phoneRegex = re.compile(r'''(
    # 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
    (\d{3}|\(\d{3}\))?                # area code(optional)
    (\s|-|\.)?                        # separator (optional)
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension optional
    )''', re.VERBOSE)

# Create a regex for email addresses

emailRegex = re.compile(r'''(
       # some.+_thing@(\d{2,5})?.com
❶     [a-zA-Z0-9._%+-]+      # username or name part
❷     @                      # @ symbol
❸     [a-zA-Z0-9.-]+         # domain name
       (\.[a-zA-Z]{2,4})      # dot-something
       )''', re.VERBOSE)


# Get the text off the clipboard

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
       phoneNum = '-'.join([groups[1], groups[3], groups[5]])
       if groups[8] != '':
           phoneNum += ' x' + groups[8]
       matches.append(phoneNum)
for groups in emailRegex.findall(text):
       matches.append(groups[0])

# Loop to find the email addresses

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
