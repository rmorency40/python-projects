#!/usr/bin/env python3

cars = ["Toyota", "Nissan", "Ford", "Lexus", "Chevrolet", "Porsche", "BMW"]
for model in cars:
    print(model)
    
print("The number of cars model in this car array is: " + str(len(cars)))

#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))
#sum = a + b
#print("The sum betwenn teh numbers: a & b is: " + str(sum))


##### Addind a constant value K =5 to each element in a lists

test_list = [1, 6, 9, 7, 10, 0]

print("The original list is : " + str(test_list))

K = 5

res = [x + K for x in test_list]

print("The new  list is : " + str(res))


### Summation of int in heterogenous lists


test_list1 = [1, 6, 9, "hete", "number", 7, 10, 0]

result = 0
for element in test_list1:
    try:
        result += int(element)
    except:
        pass
    
print("The sum of integers is: " + str(result))


# Python3 code to demonstrate working of 
# Pair summation of list 
# Using loop

List_of_numbers = [1, 6, 8, 9, 10, 8]

# Pair summation of list 
# Using loop
print("The original list is: " + str(List_of_numbers))
result = []
for ele in range(0, len(List_of_numbers), 2):
    result.append(List_of_numbers[ele] + List_of_numbers[ele + 1])

print("The pair summation of the list List_of_numbers is: " + str(result))    




