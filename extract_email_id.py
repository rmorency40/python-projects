#!/usr/bin/python3

# Extract email-id from URL text file

# library that handles the URL stuff

import urllib.request


# Importing module required for 
# regular expressions

import re

# Assign urlopen to a file object variable

fhand = urllib.request.urlopen
('https://cdncontribute.geeksforgeeks.org/wp-content/uploads/e-mail-1.txt')


for line in fhand:
    # Getting the text file
    # content line by line
    s = line.decode().strip()

    # regex for extracting all email-ids
    # from teh text file
    reg = re.findall(r"[A-Za-z0-9._%+-]+"
                     r"@[A-Za-z0-9._]+"
                     r"\.[A-Za-z]{2, 4}", s)

    #printing the list
    print(reg)
