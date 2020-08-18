#!/usr/bin/env python3

#Create a list of animals

animals = ['Eagle','Lion','Dove','Lamb','man']

print(animals[3])
print(animals[1])
animals[3] = 'Man'
print(animals[3])

animals.append('cat')
print(animals[-1])

animals.extend(['cow','horse','pig'])
print(animals)

more_animals = ['tiger','rabbit','duck','dog']

animals.extend(more_animals)
print(animals)


animals.insert(2, 'bear')
print(animals)

some_animals = animals[1:6]

print('Some animals:          {} .'.format(some_animals))

first_two = animals[0:2]
print('Fisrt two animals of the list:   {}.'.format(first_two))
fisrt_two_again  = animals[:2]
print('The first two again aninals in the list:   {}.'.format(fisrt_two_again))

last_two = animals[-2:]
print('Last two animals in the list:   {}.'.format(last_two))

# String slices

part_of_an_eagle = 'eagle' [2:5]

print(part_of_an_eagle) 

#Handling Exception
new_animal_list = ['eagle', 'bear', 'duck', 'pig', 'lion', 'tiger', 'lamb']
bear_index = new_animal_list.index('bear')
print(bear_index)

try:
    cat_index = new_animal_list.index('cat')
except:
    cat_index = 'No cats found.'

print(cat_index)


# Loops

for animal in new_animal_list:
    print(animal.upper())


index = 0
print('=' * 60)
while index  < len(new_animal_list):
    print(new_animal_list[index])
    print()
    
    
    index += 1

# Sorting and Ranges

sorted_animals = sorted(new_animal_list)
print('Animals list:           {}.'.format(new_animal_list))
print('Sorted animals list:    {}.'.format(sorted_animals))
new_animal_list.sort()
print('Animals after sort method:     {}.'.format(new_animal_list))

new_animals = ['rabbit', 'bee']
all_animals = new_animal_list + new_animals
print(all_animals)

print(len(new_animal_list))

print(len(all_animals))

# Ranges

print('==  ' * 50)
for number in range(7):
    print(number)


print('** ' * 20)

for number in range(3, 10):
    print(number)


print('** ' * 30)
for number in range(1, 50, 5):
    print(number)


print('## ' * 25)

new_animal_list = ['eagle', 'bear', 'duck', 'pig', 'lion', 'tiger', 'lamb']

for number in range(0, len(new_animal_list),  2):
    print(new_animal_list[number])
