class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, another_point):
        d = ((self.x - another_point.x)**2 + (self.y - another_point.y)**2)**0.5
        return d


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

p1 = Point(x1, y1)
p2 = Point(x2, y2)
print(p1.distance(p2))