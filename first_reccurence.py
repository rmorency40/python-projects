#!/usr/bin/python

def first_reccurence(string):
    #if not string:
        #print("this is not a string")
    counts = {}  # a dictionnary to count number of time a given
                 # character is occured
    for i in string:
        if i  in counts:
            return i
        else:
            #print(counts)
            counts[i] = 1
            
    #return '\0'

# Driver code

print(first_reccurence("ABEDFGHIOVUTYZTA"))
