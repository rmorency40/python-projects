#!/usr/bin/env python3

#Define an animal class

class Animal:
    name = ""
    color = ""
    height = 2.00
    age = 13.00
    def description(self):
        #self.name = name
        #desc_str = "%s is a %s dog with %.2f  feet and it's old of %.2f years old." %        
        #(self.name, self.color, self.height, self.age)
        desc_str = "{} is a {} dog with {}  feet and it's old of {} years old.".format(self.name, self.color, str(self.height), str(self.age))
        return desc_str

    def __str__(self):
        pass

animal1 = Animal()
animal1.name = "Medor"
animal1.color = "white"
animal1.height = 1.10
animal1.age = 10.00

animal2 = Animal()
animal2.name = "Bicky"
animal2.color = "black"
animal2.height = 2.20
animal2.age = 12.00


print(animal1.description())
print(animal2.description())
print("+=+ " * 20)

#print ("This is a good sample python class")

# Inheritance

class  mammalian(Animal):
    kind = ""
    def mamma_heart(self):
        heart_formation = "{} mammals possess a four-chambered heart.".format(self.kind)
        return heart_formation
    
mammalian1 = mammalian()
mammalian1.kind = "Teresstrial"
print(mammalian1.mamma_heart())
mammalian1.kind = "Aquatic"

print(mammalian1.mamma_heart())
print("--=  " * 20)

# instance mammalian1 from subclass mammalian with parent class Animal exuce method
# descriptipn from parent class Animal
mammalian1.name = "Leroy"
mammalian1.color = "white"
mammalian1.height = 2.00
mammalian1.age = 10.00
print(mammalian1.description())
        
        
    
    
    
    
    
    
