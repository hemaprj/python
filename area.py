base=10
height=5
area=1/2*(base*height)
print("Area is :" , area)
num=input("Enter a number: ")
num=int(num)
if num%2==0:
    print("Number is even")
else:
    print("Number is odd")


print(__name__)

import math

def circle_calc():
    r=input("Please enter radius of circle: ")
    print("__name__: ", __name__)
    print("Area of circle is  ", math.pi * (int(r) ** 2))
    print("Circumference of a circle is " , math.pi*math.pi*int(r))
    print("Diameter of a circle is " , 2*int(r))



