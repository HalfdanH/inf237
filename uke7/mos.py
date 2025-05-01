import sys
import math

class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self , v):
        return math.sqrt((self.x - v.x)**2 + (self.y - v.y)**2) 
    
class Circle:
    def __init__(self, diameter, x=0, y=0):
        self.x = x
        self.y = y
        self.diameter = diameter
        self.radius = diameter/2
    
    def isinside(self, vector):
        if Vec(self.x, self.y).distance(vector) <= self.radius: # If distance from center is smaller or equal than radius
            return True
        return False
    
def check_circle(circle, mosqitos): # Count how many mosiqitos inside
    curr = 0
    for a in range(len(mosqitos)):
                  if circle.isinside(mosqitos[a]):
                        curr += 1
    return curr


cases = int(sys.stdin.readline())

for _ in range(cases):
    sys.stdin.readline()
    n_mosqitos, bowl_diameter = sys.stdin.readline().split()
    n_mosqitos = int(n_mosqitos)
    bowl_diameter = float(bowl_diameter)
    mosqitos = []
    circle = Circle(bowl_diameter)
    for i in range(n_mosqitos):
        x, y = map(float, sys.stdin.readline().split())
        mosqitos.append(Vec(x, y))
    best = 1

    for i in range(len(mosqitos)-1):
        vec1 = mosqitos[i]
        for o in range(i+1, len(mosqitos)):
            vec2 = mosqitos[o]
            distance = vec1.distance(vec2)
            if distance <= circle.diameter: # Check that distance is less or equal to diameter, or not 
                
                mx = (vec1.x + vec2.x) /2 #Mid point between two points
                my= (vec1.y + vec2.y) /2 
                h = math.sqrt(circle.radius**2-(distance/2)**2) #

                circle.x = mx + h * (-(vec2.y - vec1.y)/distance) # Circle 1
                circle.y = my + h * ((vec2.x - vec1.x)/distance)

                curr = check_circle(circle, mosqitos)
                if curr > best:
                    best = curr

                circle.x = mx - h * (-(vec2.y - vec1.y)/distance) # Circle 2
                circle.y = my - h * ((vec2.x - vec1.x)/distance)
                curr = check_circle(circle, mosqitos)
                if curr > best:
                    best = curr

            
    print(best)


