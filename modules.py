#!/usr/bin/env python3

import time
print(time.asctime())
print(time.timezone)

print('==' * 15)

from time import asctime
print(asctime())


print('**' * 50)
from time import asctime, sleep
print(asctime())
sleep(2)
print(asctime())

print('+=+' * 16)

import  sys
for path in sys.path:
    print(path)
    

print('##' * 20)

import sys
file_name = 'test.txt'
try:
    with open(file_name) as test_file:
        for line in test_file:
            print(line)
except:
    print('Could not open {}'.format(file_name))
    sys.exit(1)


#Call module named say_hello.py

print('&*=' * 20)

import say_hello

say_hello.say_hello()

#Main function
print('*&' * 20)

def say_hi():
    print('Hi !')
def   main():
    print('Hello from say_hi3.py')
    say_hi()

if __name__ == '__main__':
    main()
   

# Exo

def cat_say(text):
    """Generate a picture of a cat saying something"""
    text_length = len(text)
    print(' {}'.format('_' * text_length))
    print(' < {} >'.format(text))
    print(' {}'.format('-' * text_length))
    print(' /')
    print(' /\_/\ /')
    print('( o.o )')
    print(' > ^ <')
def main():
    text = input('What would you like the cat to say? ')
    cat_say(text)
if __name__ == '__main__':
    main()



import cat_say

def main():
    cat_say.cat_say('Feed me.')
    cat_say.cat_say('Pet me.')
    cat_say.cat_say('Purr. Purr.')
if __name__ == '__main__':
    main()


##### Some math
print('Let\'s have the computer doing so maths')

import math
print (math.sin(90))
print(math.cos(0))
print(math.pow(2,5))
