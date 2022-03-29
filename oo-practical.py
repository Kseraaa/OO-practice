import math

class Shape:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def cal_area(self):
        pass
class Rectangle:
    def __init__(self, wide, long):
        self.wide = wide
        self.long = long

    def cal_area(self):
        return self.wide * self.long

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def cal_area(self):
        return math.pi * self.radius * self.radius

