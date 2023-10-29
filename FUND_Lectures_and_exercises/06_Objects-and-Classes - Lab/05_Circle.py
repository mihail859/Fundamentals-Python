class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        c = 2 * Circle.__pi * self.diameter/2
        return c

    