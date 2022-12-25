import math

def circle_area(x):
   area = math.pi * (x*x)
   print(area)

def circle_perimeter(x):
   perimeter = math.pi*2*x
   print(perimeter)

def triangle_perimeter(x,y,z):
   perimeter = x+y+z
   print(perimeter)

def triangle_area(x,y,z):
   s = (x+y+z) /2 
   area=(s*(s-x)*(s-y)*(s-z))**(1/2) 
   print(area)

def square_perimeter(x):
   perimeter = 4 * x
   print(perimeter)

def square_area(x):
   area = x * x
   print(area)
  
  
