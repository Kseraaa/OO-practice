import math
from abc import ABC, abstractmethod

class Shape:
    def __init__(self,name) :
        self.name = name
    
    def cal_area(self) :
        pass

class Rectangle(Shape) :
    def __init__(self,name,width,length) :
        super().__init__(name)
        self.width = width
        self.length = length
        
    def cal_area(self) :
        return (self.width)*(self.length)

class Circle(Shape) :
    def __init__(self, name,radius):
        super().__init__(name)
        self.radius = radius
    def cal_area(self):
        return (math.pi)*((self.radius)**2)

def cal_total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.cal_area()
    return total

r1 = Rectangle('r1',4,5)
r2 = Rectangle('r2',10,12)
c1 = Circle('c1',10)
print(r1.cal_area())
print(r2.cal_area())
print(c1.cal_area())
shapes = [r1,r2,c1]
total_area = cal_total_area(shapes)
print(total_area)




