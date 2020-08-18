#!/usr/bin/python
import sys
sys.setrecursionlimit(10**4)

def binary_search1(item_list, lower, higher, item):
    if higher >= lower:
        mid = (lower + (higher -1)) // 2
        if item_list[mid] == item:
            return 'item is found'
        elif item_list[mid] > item:
            return binary_search1(item_list, lower, mid - 1, item)
        else:
            return binary_search1(item_list, mid + 1, higher, item)
    else:
        return 'item is not found'

# Driver code 123
item_list = [1, 2, 7, 12, 28, 31, 40, 41, 42, 46, 59]
item = 46
lower = 0
higher = len(item_list) - 1
print(binary_search1(item_list, lower, higher, item))

#print(stars)
#print(stars)

item_list2 = [1, 2, 7, 12, 28, 31, 40, 41, 42, 46, 59]
item = 60
lower = 0
higher = len(item_list2) - 1
print(binary_search1(item_list2, lower, higher, item))
