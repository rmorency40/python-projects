#!/usr/bin/env python3

import math

def binary_search1(item_list, lower, higher, item):
    if higher >= lower:
        mid = math.ceil(lower + (higher - 1) / 2)
        #print(mid)
        if (item_list[mid]) == item:
            #print(mid)
            print(item)
            return 'item is found'
        elif item_list[mid] > item:
            return binary_search1(item_list, lower, mid - 1, item)
        else:
            return binary_search1(item_list, mid + 1, higher, item)
    else:
        return 'item is not found'

# Driver code
item_list = [1, 2, 7, 12, 28, 31, 40, 41, 42, 46, 59]
lower = 0
#higher = len(item_list) - 1
higher = len(item_list) - 1
item = 32
print(binary_search1(item_list, lower, higher, item))
