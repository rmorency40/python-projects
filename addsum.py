#!/usr/bin/python3

def addsum(array, target):
    if not array or len(array) < 1:
        print("empty array")
    for i in range(len(array)):
        for j in range(1, len(array)):
            if array[i] + array[j] == target:
                return [i,j]
#Drive code
array = [11, 15, 4, 6, 7, 5, 8, 1]
target = 9
a = addsum(array, target)
print(a)


############ Given a 32-bit signed ineger, reverse digits of an integer.

n = 155
rev = 0
while(n >  0):
    a = n % 10
    rev = rev * 10 + a
    n = round(n / 10)

print(rev)
