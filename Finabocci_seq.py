#!/usr/bin/env python3

def recur_fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2))  
# take input from the user  
nterms = int(input("How many terms? "))  
# check if the number of terms is valid  
if nterms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(recur_fibo(i))  

firstname = input("What is your name: ")
print("Your first name is " + firstname)
lastname = input("What is your last name: ")
print("Your last name is " + lastname)
print("Your full name is: " + firstname  + lastname)