exercise 1

def even(list):
    my_list =[ ]
    even = my_list[: : 2]
    print(even)
return even

exercise 2

def greatest(list):
    my_list =[ ]
    i=0
    k = int(input("enter a number"))
    for i in range(len(my_list)):
        if my_list[i] > k:
           greatest = my_list[i]
        else:
            print("greatest does not exist")
    return greatest
  
  exercise 3
  
  def swap_min_max(a):
    max_index =a.index(max(a))
    min_index =a.index(min(a))
    ma=max(a)
    mi=min(a)
    a[max_index]=mi
    a[min_index]=ma
    a=[ ]
    print(a)
    return swap_min_max(a)
  
  exercise 4
  
   def value(dict,key):
        dict ={}
        print(dict["key"])
        return value
      
      exercise 5
    
from math import pi
default_radius =5
def circle_area(r = default_radius):
    return (pi*(r**2))
def circle_perimeter(r = default_radius):
    return 2*pi*r

default_a =15
def square_area(a =default_a):
    return a*a
def square_perimeter(a = default_a):
    return 4*a


from math import sqrt
a=7
b=2
c=8
def triangle_perimeter(a=a, b=b, c=c):
    return a+b+c
def triangle_area(a=a, b=b, c=c):
    return sqrt(4*a**2*b**2 -(a**2+b**2-c**2)*2)/4


    test.py
from figures.circle.code import *
from figures.triangle.code import *
from figures.square.code import *

from figures import circle_area,square_perimeter,triangle_area

print(f"the area of the circle is : {circle_area()} ")

print(f"the perimeter of the square is : {square_perimeter(10)}")

print(f"the area of the triangle is : {triangle_area()}")

