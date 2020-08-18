#!/usr/bin/env python3

weekend_tuple = ('Saturday', 'Sunday')
weekend_list = list(weekend_tuple)

print('weekend_tuple is {}.'.format(type(weekend_tuple)))
print('weekend_list is {}.'.format(type(weekend_list)))



weekend_days = ('Saturday', 'Sunday')      
for days in weekend_days:
    print(days)




def high_and_low(numbers):
    """ Determine the highest and the lowest number """
    highest = max(numbers)
    lowest = min(numbers)
    return(highest, lowest)

lottery_numbers = [16, 4, 42, 15, 23, 8]
(highest, lowest) = high_and_low(lottery_numbers)
print('The highest number is : {}.'.format(highest))
print('The lowest number is:{}.'.format(lowest))


contacts = [('Jason', '556-0987'), ('Carl', '908-1234')]


for (name,phone) in contacts:
    print("{}'s phone number is {}.".format(name,phone))
                                    
                                    
                                    
# tuple exercice

print()
airport_list = [('Port-au-Prince International Airport', 'PAP'),
                ('Orlando International Airport', 'MCO'),
                ('Austin-Bergstrom International Airport', 'AUS'),
                ('Denver International Airport', 'DEN'),
                ('Los Angeles International Airport', 'LAX'),
                ('Dallas/Fort Worth International Airport', 'DFW'),
                ('New York International Airport', 'JFK')]
for (airport,code) in airport_list:
    print('The code for {0} is {1}.'.format(airport, code))
                                    
                                    
