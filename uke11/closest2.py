import sys
import math
from dataclasses import dataclass

sys.setrecursionlimit(3000) 

@dataclass(frozen=True)
class Vec:

    x: float
    y: float
    
    def __str__(self):
        return f"Point: x: {self.x}, y: {self.y}"

    def __lt__(self, vec2):
        return self.x < vec2.x+1e-5

    
    
def dist(v1, v2):
    return (v1.x - v2.x)**2 + (v1.y - v2.y)**2


def bruteforce(points, start, end):
    smallest = float("inf")
    for i in range(start, end-1):
        for o in range(i+1, end):
            if dist(points[i], points[o]) < smallest + 1e-5: 
                smallest = dist(points[i], points[o]) 
                left = points[i]
                right = points[o]

    return smallest, left, right


def dc(pointsx, start, end):
    n = len(pointsy)
    if n <= 3:
        return bruteforce(pointsy)
    
    mid = n//2
        
    left_result = dc(pointsx, start, mid)
    right_result = dc(pointsx, mid, end)

    if left_result[0] < right_result[0]:
        smallest, left_point, right_point = left_result
    else:
        smallest, left_point, right_point = right_result
    
    return smallest, left_point, right_point
    
    
while n := int(sys.stdin.readline()):
    points = []
    for i in range(n):
        x, y = map(float, sys.stdin.readline().split())
        point = Vec(x, y)
        points.append(point)
    pointsx = sorted(points, key=lambda p: (p.x, p.y))
    pointsy = sorted(points, key=lambda p: (p.y, p.x))

    
    min_dist, vec1, vec2  = dc(pointsx)

    print(vec1.x, vec1.y, vec2.x, vec2.y)
