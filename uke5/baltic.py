import sys
import heapq

#MST
# Traverse 
h, w = map(int ,sys.stdin.readline().split())

m = []
for _ in range(h):
    row = list(map(int, sys.stdin.readline().split()))
    m.append(row)

i, j = map(int ,sys.stdin.readline().split()) # Start 
i = i-1
j = j-1

total = 0
highest = m[i][j]
heap = [(highest, i, j)]
heapq.heapify(heap) # Start with the smallest values
visited = set() 
visited.add((i, j))
while heap:
    point, i, j = heapq.heappop(heap)
    if point > highest:
        highest = point #Update the highest point as we cant get more water than that
    if highest < 0:
        total += -highest
        
    for o in range(i-1, i+2):
        for u in range(j-1, j+2):
            if o >= 0 and o < h and u >= 0 and u < w:
                if (o, u) not in visited:
                    point =  m[o][u]
                    visited.add((o, u))
                    heapq.heappush(heap, (point, o, u))

print(total)




