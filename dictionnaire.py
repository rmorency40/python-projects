#!/usr/bin/env python3

"""thisdic = {
    "brand": "Nissan",
    "model": "Rogue",
    "year": 2013
  }

thisdic["color"] = "gray"
thisdic["transmission"] = "automatic"
print(thisdic)
print(thisdic.get("model"))

thisdic.clear()
print(thisdic)

thisdic["Owner"] = "RR"
print(thisdic)

del thisdic["Owner"]
print(thisdic)

thisdic["Coowner"] = "JM"
thisdic["Owner"] = "RR"
print(thisdic)

thisdic.popitem()
print(thisdic) '"""

contacts = {'Jason': '555-0144',
            'Karl': '557-0987'
            }
jasons_phone = contacts['Jason']
karls_phone = contacts['Karl']

print('Dial {} to call Jason.'.format(jasons_phone))

print('Dial {} to call Karl.'.format(karls_phone))

new_contacts = {'Jason': ['777-0955', '776-9876'],
                'Karl': '987-0987'
                }

print(len(new_contacts))
print(new_contacts['Jason'])
print(new_contacts['Karl'])


if 'Jason' in new_contacts.keys():
    print("Jason's phone number is:")
    print(new_contacts['Jason'] [0])

if 'Tony' in new_contacts.keys():
    print("Tony's phone number is")
    print(new_contacts['Tony'] [0])


print(['777-0955','776-9876'] in new_contacts.values())


for contact in new_contacts:
    print('The number for {0} is {1}.'.format(contact, new_contacts[contact]))

for person,phone_number in new_contacts.items():
    print('The number for {0} is {1}.'.format(person, phone_number))


other_contacts = {
    'RR':{
        'phone': '555-0987',
        'email': 'rr@gmail.com'
     },
    'JHM':{
        'phone': '987-1234',
        'email': 'jhm@gmail.com'
      }
    }

for person,phone_number in other_contacts.items():
    print('The contact for {0} is {1}.'.format(person, phone_number))

for contact in other_contacts:
    print("{}'s contact info:".format(contact))
    print(other_contacts[contact] ['phone'])
    print(other_contacts[contact] ['email'])
    

# Dictionnary exo

people = {"Jeff": " really gentil",
          "Jenny": "very pickey",
          "Leo": "a funny guy",
          "Jack": "a brillant student",
          "RR": "a faithful man"
          }

for person in people.keys():
    print("{0} is {1}.".format(person, people[person]))
    
people["Leo"] = 'a realistic guy'

print("*" * 50)
print("*" * 50)
for person in people.keys():
    print("{0} is {1}.".format(person, people[person]))

people["John"] = "an excellent teacher"

print("==" * 30)
for person in people.keys():
    print("{0} is {1}.".format(person, people[person]))

print()
print()
# other solution

def display_facts(facts):
    
    """Displays facts"""
    for fact in facts:
        print('{}: {}'.format(fact, facts[fact]))
    print()
    
facts = {
    'Jason': 'Can fly an airplane.',
    'Jeff': 'Is afraid of clowns.',
    'David': 'Plays the piano.'
}

display_facts(facts)
facts['Jeff'] = 'Is afraid of heights.'
facts['Jill'] = 'Can hula dance.'
display_facts(facts)
