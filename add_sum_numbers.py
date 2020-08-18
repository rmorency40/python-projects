#!/usr/bin/python

## sum of 2 numbers in a given array

def add_sum_numbers(array, target):
    if not array:
        print(" This is not an array")
    dict = {}
    for i in range(len(array)):
        dict[array[i]] = i
        print(dict)
        complement = target - array[i]
        if complement in dict:
            print(complement)
            return [dict[array[i]], dict[complement]]
        
            
            



# driver code

array = [1, 2, 9, 10, 7, 3]
target = 10
print(add_sum_numbers(array, target))
        
