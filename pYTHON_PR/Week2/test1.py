import math
class Point2D():
    def __init__(self, x, y):
        self.x =x
        self.y=y

    def calculate_distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx*dx+dy*dy)
point1=Point2D(3,4)
point2=Point2D(9,5)
d = point1.calculate_distance(point2)
print(d)
