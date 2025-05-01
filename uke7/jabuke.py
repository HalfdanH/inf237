import sys
import math
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

    def distance(self,  vec):
        return math.sqrt((self.x - vec.x)**2 + (self.y - vec.y)**2)

    
def cross(vec1, vec2):
    return vec1.x * vec2.y - vec1.y * vec2.x

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
def orient(a, b, c):
    return cross(Vector(b.x-a.x, b.y-a.y), Vector(c.x-a.x, c.y- a.y))


def in_angle(a, b, c, p):
    return orient(a, b, p) + 1e-5 >= 0  and orient(a, c, p)  <=0 + 1e-5

def inside(triangle, p):
    a = triangle.a
    b = triangle.b
    c = triangle.c
    
    return in_angle(a, b, c, p) and in_angle(c, a, b, p)

xa, ya = map(float,sys.stdin.readline().split()) 
xb, yb = map(float,sys.stdin.readline().split()) 
xc, yc = map(float,sys.stdin.readline().split()) 

n = int(sys.stdin.readline())
trees = []
for _ in range(n):
    x, y = map(float,sys.stdin.readline().split()) 
    trees.append(Vector(x, y))

area = (xa*(yb-yc) + xb*(yc-ya) + xc*(ya-yb))/2 # Formula for area
print(abs(area)) # Might be negative if points are counterclock

if area > 0:
    triangle = Triangle(Vector(xa, ya), Vector(xb, yb), Vector(xc, yc)) 
else:
    triangle = Triangle(Vector(xa, ya), Vector(xc, yc),  Vector(xb, yb)) # Swap point b and c to get clockwise

total = 0
for point in trees:
    if inside(triangle, point):
        total+=1

print(total)
    