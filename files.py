#!/usr/bin/env python3

#hosts = open(r'''C:\Users\rmorency\Documents\TOM\tom_queries.txt''')
"""hosts_file_contents = hosts.read()
print(hosts_file_contents)

print('*' * 30)
print('Current position: {}.'.format(hosts.tell()))
print(hosts.read())

print('-' * 25)
print('Current position: {}.'.format(hosts.tell()))
print(hosts.read())

print('=' * 35)
hosts.seek(0)
print('Current position: {}.'.format(hosts.tell()))
print(hosts.read()) """

"""print(hosts.read())
print('File closed? {}.'.format(hosts.closed))
if not hosts.closed:
    hosts.close()
    
print('File closed? {}.'.format(hosts.closed))    
#print(hosts.tell())
#hosts.close()"""

"""print('==' * 50)
print('Started reading the file:')
with open(r'''C:\Users\rmorency\Documents\TOM\tom_queries.txt''') as hosts:
    print('File closed? {}.'.format(hosts.closed))
    print(hosts.read())
print("Finished reading the file.")
print('File closed? {}.'.format(hosts.closed))

print('*' * 30)"""

with open(r'''C:\Users\rmorency\Documents\TOM\tom_queries.txt''') as the_file:
    for line in the_file:
        #print('there is ')
        print(the_file.mode)
        print(line.rstrip())

# Mode files
with open(r'''C:\Users\rmorency\Documents\TOM\tom_queries.txt''') as the_file:
    the_file.write('The following lines are not sql statement,they have been added to teh file.')
    the_file.write('Select * from dual')
    
print(the_file.read())
