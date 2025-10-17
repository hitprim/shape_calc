import math
from abc import abstractmethod, ABC


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
    
class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
        
    def area(self) -> float:
        return math.pi * self.radius ** 2
    
class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        sides = [a, b, c]
        if any(side <= 0 for side in sides):
            raise ValueError("Sides must be positive")
        if not self.not_triangle(sides):
            raise ValueError("Invalid triangle sides")
        self.sides = sides
        
    def area(self) -> float:
        a, b, c = self.sides
        p = (a +b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    def is_right(self) -> bool:
        a, b, c = sorted(self.sides)
        return abs(a**2 + b**2 - c**2) < 1e-7
    
    @staticmethod
    def is_valid(sides)->bool:
        a, b, c = sorted(sides)
        return a + b > c
    
def calc_area(shape: Shape) -> float:
    return shape.area()


circle = Circle(5)
print(f'Circle area: {calc_area(circle):.2f}')
            