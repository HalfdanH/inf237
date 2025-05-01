import sys
from collections import defaultdict
import heapq


n = int(sys.stdin.readline())
squares = []
for i in range(n):
    squares.append(int(sys.stdin.readline()))


situations = defaultdict(lambda: float("inf")) # Inf so "all" values are better and for keyerror

situations[0, 0] = 0 # Start at first position


heap = [(0, 0, 0)] # Heap sorted by cost
heapq.heapify(heap)
smallest = float("inf")
while heap:
    smallest = heapq.heappop(heap)
    cost, pos, jump = smallest 
    
    forward = pos+jump+1 # Next forward position
    if forward < n:
        if forward == n-1: # If reach last stone
            smallest = cost + squares[forward]
            break #Break since heap the cheapest is the first one to reach it
        new_cost = cost + squares[forward]
        if new_cost < situations[forward, jump+1]: # If it is better than another way to reach
            situations[forward, jump+1] = new_cost
            new_sit = (new_cost, forward, jump+1)
            heapq.heappush(heap, new_sit) # Add the new situation to heap
        

    backward = pos-jump
    if backward >= 0: #valid back jump # does actually jump to 0 from 0 every time so like could be optimized
        new_cost = cost + squares[backward]
        if new_cost < situations[backward, jump]: # Same except jump size is same and stone is back
            situations[backward, jump] = new_cost
            new_sit = (new_cost, backward, jump)
            heapq.heappush(heap, new_sit)

    

print(smallest)