# Exo1
animal = 'eagle'
vegetable = 'brocoli'
mineral = 'gold'

print('Here is  an animal,a vegetable and a mineral .')
print(animal)
print(vegetable)
print(mineral)

# Exo 2

user_input = input('Please type something and press Enter:  ')
print('=' * 75)
print('You entered:')
print(user_input)

# Exo 3

# GEt the input from teh user

text = input('What would you like teh cat to say? ')

# DEtermine the length of the input

text_length = len(text)

# Make the boeder the same size as  the input

print('              {}'.format('_' * text_length))
print('             < {} > '.format(text))
print('            {}' .format('-' * text_length))
print('           /')
print('/\_/\     /')
print('( o.o )')
print('> ^ < ')
