#!/usr/bin/python python3

# Define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 10000.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color,
                                                   self.kind, self.value)
        return desc_str

# 1st instance of Vehicle class
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

# 2nd instance of Vehicle class

car2= Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 11000.00

# test the codes

print(car1.description())
print(car2.description())

