#!/usr/bin/env python3

import math

def triangle(b,h):
    area = (b*h) / 2
    return area

def rectangle(b,h):
    area = (b*h)
    return area
def circle(r):
    area = math.pi * r**2
    return area

def main():
    status =  True
    while(status):
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if(shape == "triangle"):
            base = float(input("Give base of the triangle: "))
            height = float(input("Give height of the triangle: "))
            result = triangle(base, height)
            print("The area is {:.3f}".format(result))
        elif (shape == "rectangle"):
            base = float(input("Give base of the rectangle: "))
            height = float(input("Give height of the rectangle: "))    
            result = rectangle(base, height)
            print("The area is {:.3f}".format(result))           
        elif (shape == "circle"):
            radio = float(input("Give the radius of the circle: "))
            result = circle(radio)
            print(f"The area is {result}") 
        elif (shape ==""):
            status = False
        else:
            print("Unknown shape!")




if __name__ == "__main__":
    main()
