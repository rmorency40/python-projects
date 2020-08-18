#!/usr/bin/env python3

import re

print('caret character' * 5)
print('**' * 20)
beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello there !'))


print('%*% ' * 20)
endsWithWorldRegex = re.compile(r'world$')
print(endsWithWorldRegex.search('Hello world'))


print('@Regex ' * 10)
allDigitRegex = re.compile(r'^\d+$')
print(allDigitRegex.search('12345678909876543'))

print('.dot ' * 10)

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))

print('one or 2 anything, ' * 3)

atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))

print('dot* , ' * 7)

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: Rony  Last Name: Morency'))

print('dot* is greedy by default , ' * 2)
serve = '<To serve humans> for diner.>'
nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))


print('dot* is greedy by default , ' * 2)
greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))

print('dot - all exceptnew line' * 2)
prime = 'Serve the public trust. \nProtect the innocent.\nUpload the law.'
print(prime)
print('BLA ' * 20)
dotStarRegex = re.compile(r'.*')
print(dotStarRegex.search(prime))

print('mathc everything even new line ' * 2)
dotstarRegex = re.compile(r'.*', re.DOTALL)
print(dotstarRegex.search(prime))

print('match lower and upper case, ' * 2)
sentence = 'Rony MORENCY'
vowel = re.compile(r'[aieou]', re.I)
print(vowel.findall(sentence))
print
