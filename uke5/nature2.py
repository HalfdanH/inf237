import sys
import heapq
from collections import defaultdict
import time

# Path compression forelesning Kruskals
def find_parent(node, comp):
    if comp[node] == node: #If the top parent is it self
        return node
    else:
        parent = find_parent(comp[node], comp)
        comp[node] = parent # Save parent
        return parent 
    
def union(node1, node2, comp):
    parent1 = find_parent(node1, comp) 
    parent2 = find_parent(node2, comp) 
    comp[parent1] = parent2

def mst(edges, initials, n_stations, n_iniitals):
    comp = {i: i for i in range(1, n_stations+1)} # Init all nodes are their own parent
    total = 0
    for i in range(1, len(initials)):
        union(initials[0], initials[i], comp) # Add union between startnodes as they shouldnt have cost
    visited = n_iniitals
    while edges:
        if visited == n_stations: # stop when we have all edges we want
            break
        cost, first, second = heapq.heappop(edges)
        if find_parent(first, comp) != find_parent(second, comp): # If it doesnt make a loop
            total+=cost
            visited+=1
            union(first, second, comp) #Add "loop" and add cost
            
    return total

n = int(sys.stdin.readline())
for i in range(n):
    
    n_stations, n_channels, size, n_iniitals = map(int, sys.stdin.readline().split())
    initials = list(map(int, sys.stdin.readline().split()))
    edges = []
    
    
    for o in range(n_channels):
        first, second, cost = map(int, sys.stdin.readline().split())
        edges.append((cost, first, second))
    
    heapq.heapify(edges)
    print(mst(edges, initials, n_stations, n_iniitals) + size*(n_stations-n_iniitals)) # Size*number of edges plus the startcosts



    