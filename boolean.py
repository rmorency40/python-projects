#!/usr/bin/env python3

# Ask the user how long he wants to travel
travel_distance = int(input('How far do you want to go:  '))

if travel_distance < 3:
    print('I suggest working to your destination .')

elif  (travel_distance > 3) and (travel_distance < 300):
    print('I suggest driving to your destination .')

if travel_distance >= 300:
    print(' I suggest flying to your destination .')

print('Have a nice trip !')


# The same solution but another way

# Ask the distance
distance = input('How far would you like  to travel in miles? ')

# Convert the distance to an integer

distance = int(distance)

# Determine what mode of transport to use

if distance < 3:
    mode_of_tranport = 'working'
elif distance < 300:
    mode_of_tranport = 'driving'
else:
    mode_of_tranport = 'flying'

# Display teh results

print('I suggest {} to your destination.'.format(mode_of_tranport))


