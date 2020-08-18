#!/usr/bin/python

# Check if a string a valid or not

def isvalidstring(string):
    stack = []
    a = '('
    b = ')'
    c = '{'
    d = '}'
    e = '['
    f = ']'
    for i in string:
        if i == a or i == c or i == e:
            stack.append(i)
        else:
            if len(stack) != 0:
                temp = stack.pop()
                if ((i == b and a == temp) or (i == d and c == temp) or (i == f and e == temp)):
                    continue
                else:
                    return False
    return len(stack) == 0


#Dirive code

string = '{[]}'
print(isvalidstring(string))
                
                
                
