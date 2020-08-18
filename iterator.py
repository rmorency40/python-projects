#!/usr/bin/env    python3

# Iteration

mytuple = ("cow", "dog", "goat", "cat", "mouse")

myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print("///// ===" * 15)
mysentence = "I am a good  python programmer"
myit = iter(mysentence)

"""print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit)) """

print ("**** ++++" * 10)
print(" All print ...above can be replace by teh below iteration")
mysentence = "I am a good  python programmer"
for i in   mysentence:
      print(i)



print("+-+ " * 15)

class Mynumber:
    
    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a +=1
            return x
        else:
            raise StopIteration
myclass = Mynumber()
myiter = iter(myclass)

for x in myiter:
    print(x)
        
