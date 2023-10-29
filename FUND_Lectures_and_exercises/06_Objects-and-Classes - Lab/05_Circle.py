import math
class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        c = 2 * Circle.__pi * self.diameter/2
        return c

    def calculate_area(self):
        area = Circle.__pi * math.pow((self.diameter / 2), 2)
        return area

    def calculate_area_of_sector(self, angle):
        #A = (θ/360) * π * r^2
        area_sector = (angle / 360) * Circle.__pi * math.pow((self.diameter / 2), 2)
        return  area_sector


circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
