import sys
from collections import defaultdict
import math

# queue and take last to continue and add other to que start and last
class Vec:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{self.x}, {self.y}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))

    def __sub__(self, other):
        return Vec(self.x-other.x, self.y-other.y)
    

    def __lt__(self, other):
        return self.x < other.x or (self.x == other.x and self.y < other.y)

def cross(vec1, vec2):
    return vec1.x * vec2.y - vec1.y * vec2.x

def orient(a, b, c):
    return cross(Vec(b.x-a.x, b.y-a.y), Vec(c.x-a.x, c.y- a.y))

def leftturn(p1, p2, p3):
    return orient(p1, p2, p3) > 0




num_points = int(sys.stdin.readline())
edges_set = defaultdict(lambda: set())
points = []
for i in range(num_points):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    point1 = Vec(x1, y1)
    point2 = Vec(x2, y2)
    if point1 not in edges_set:
        points.append(point1)

    if point2 not in edges_set:
        points.append(point2)
    edges_set[point1].add(point2)
    edges_set[point2].add(point1)

points.sort(key=lambda p: (p.x, p.y))

edges = defaultdict(lambda: [])

for i in range(len(points)-1):
    p1 = points[i]
    for o in range(i+1, len(points)):
        p2 = points[o]
        if p2 in edges_set[p1]:
            edges[p1].append(p2)
        if p1 in edges_set[p2]:
            edges[p2].append(p1)

for point in points:
    Q = sorted([(v-point, v) for v in edges[point]], key=lambda tup: math.atan2(tup[0].x, tup[0].y))
    edges[point] = [v for _, v in Q]

visited = set()
p = points[0]
hull = [p]


while True:
    for n in edges[p]:
        if n not in visited:
            visited.add(p)
            p = n
            hull.append(p)
            break

    if len(hull) == len(points):
        break

hull.append(points[0])

for p in hull:
    print(p)
s = 0
for i in range(len(hull)-1):
    p1 = hull[i]
    p2 = hull[i+1]
    s += abs(p1.x*p2.y-p2.x*p1.y)
print(s/2)