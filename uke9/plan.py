import sys
from collections import defaultdict
import math
import heapq

n = int(sys.stdin.readline())
place_coords = {}
for _ in range(n):
    place, x, y = sys.stdin.readline().split()
    x, y = map(float, (x, y))
    place_coords[place] = (x, y)

def calc_dist(place1, place2):
    x1, y1 = place_coords[place1]
    x2, y2 = place_coords[place2]
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def calc_dist_pairs():
    pair_dist = {}
    for place in place_coords:
        for place2 in place_coords:
            if place == place2:
                continue
            dist = round(calc_dist(place, place2), 5)
            pair_dist[(place, place2)] = dist
            pair_dist[(place2, place)] = dist

    return pair_dist

pair_dist = calc_dist_pairs()

def tsp(places):
    n = len(places)
    dp={}
    dp[(1, 0)] = 0 # 0001
    heap = [(0, 0, 1)] # total distance, current node, current mask
    heapq.heapify(heap)
    cost = {}
    while heap:
        dist, node, mask = heapq.heappop(heap)
        if node == n-1: 
            if mask == (1 << n) -1: # 1000 -1 = 0111
                break
        else:
            place = places[node]
            for i in range(1, n): # Dont need to check work
                if i == node:
                    continue
                place2 = places[i]
                new_mask = mask | (1 << i) #  0001 | 0010 = 0011 
                new_dist = round(dist + pair_dist[(place, place2)],5)
                if (i, new_mask) not in dp or cost[(i, new_mask)] > new_dist: # If not visited or smaller cost
                    dp[(i, new_mask)] = node, mask # Where it came from
                    heapq.heappush(heap, (new_dist, i, new_mask))
                    cost[(i, new_mask)] = new_dist
    answer = []
    while True:
        node, mask = dp[(node, mask)]
        place = places[node]
        if place == "work":
            break
        answer.append(place)
    answer.reverse()
    print(" ".join(answer))


while True:
    places = sys.stdin.readline().split()
    if len(places) == 0:
        break
    
    places.insert(0, "work")
    places.append("home")
    tsp(places)