#!/usr/bin/python3

# Function to check if all teh list values are the same
# 1st approach

def all_array_the_same(elements):
    if len(elements) < 1:
        return true
    return len(elements) == elements.count(elements[0])
# Delimiter

delimiter = """**************
            ------------------
             =================="""
print(delimiter)
# Drive code
elements = [2, 2, 2]
a = all_array_the_same(elements)
print(a)

# Function to check if all teh list values are the same
# 1st approach
print(delimiter)

def all_list_the_same(list):
    if not list:
        return true
    return [list[0]] * len(list) == list
#Driven code

lists = [1,1,1,1,1,1,1]
b = all_list_the_same(list)
print(b)
print(delimiter)
list2 =  [1, 4, 5, 8, 10]
c = all_list_the_same(list2)
print(list2)
