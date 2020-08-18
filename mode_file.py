#!/usr/bin/env python3

with open(r'''C:\Users\rmorency\Documents\TOM\tom_queries1.txt''', 'w') as the_file:
    
    the_file.write('The following lines are not sql statement,they have been added to the file.\n')
    the_file.write('Select * from dual.\n')

with open(r'''C:\Users\rmorency\Documents\TOM\tom_queries1.txt''') as the_file:
    print(the_file.read())


#Open a file and assign its contents to a variable.
#If the file is unavailable,create an empty variable.


try:
    contacts = open('contacts.txt').read()
except:
    contacts = ''

print(len(contacts))

print('*' * 50)
##### Exo1


with open('file.txt') as file:
    line_number = 1
    for line in file:
        print('{}: {}'.format(line_number, line.rstrip()))
        line_number += 1
    

#Exo 2


#!/usr/bin/env python3
unsorted_file_name = 'animals.txt'
sorted_file_name = 'animals-sorted.txt'
animals = []
try:
    with open(unsorted_file_name) as animals_file:
        for line in animals_file:
            animals.append(line)
            animals.sort()
except:
    print('Could not open {}.'.format(unsorted_file_name))
try:
    with open(sorted_file_name, 'w') as animals_sorted_file:
        for animal in animals:
            animals_sorted_file.write(animal)
except:
    print('Could not open {}.'.format(sorted_file_name))
        
