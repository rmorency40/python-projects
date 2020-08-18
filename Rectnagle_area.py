#!/usr/bin/python v3

print("Enter 'x' for exit.")
leng = input("Enter length of Rectangle: ");
if leng == 'x':
    exit();
else:
    brea = input("Enter breadth of Rectangle: ");
    length = int(leng);
    breadth = int(brea);
    area = length*breadth;
    print("\nArea of Rectangle =" , area);
    
