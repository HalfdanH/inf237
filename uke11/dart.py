import sys
import math

class Vec:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point x={self.x}, y={self.y}"


def cross(vec1, vec2):
    return vec1.x * vec2.y - vec1.y * vec2.x

def orient(a, b, c):
    return cross(Vec(b.x-a.x, b.y-a.y), Vec(c.x-a.x, c.y- a.y))

def leftturn(p1, p2, p3):
    return orient(p1, p2, p3) >= 0

def dist(vec1, vec2):
    return math.sqrt((vec1.x - vec2.x)**2 + (vec1.y-vec2.y)**2)


def graham(points):
    n = len(points)
    points = sorted(set(points), key=lambda p: (p.x, p.y))
    S, hull = [], []

    for p in points: # Hupper part
        while len(S) > 1 and leftturn(S[-2], S[-1], p):
            S.pop()
        S.append(p)
    hull+= S

    
    S = []
    for p in reversed(points): # Lower part
        while len(S) > 1 and leftturn(S[-2], S[-1], p):
            S.pop()
        S.append(p)
    hull+= S[1:] # Skip the first #rightmost points as it is in hull form lower part but add last since its closed
    
    t_dist = 0

    for i in range(len(hull)-1):
       t_dist += dist(hull[i], hull[i+1])

    return (100*n)/(1+t_dist) # Score formula

while True:
    data = list(map(float, sys.stdin.readline().split()))
    points = []
    if len(data) == 0:
        break
    for i in range(0, len(data), 2):
        x = data[i]
        y = data[i+1]
        point = Vec(x, y)
        points.append(point)
    print(graham(points))