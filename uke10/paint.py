import sys
import queue
from collections import defaultdict
n, m = map(int, sys.stdin.readline().split())

edge_cap = defaultdict(lambda:0) # Capacity, initial 0 for every
edges = defaultdict(lambda: [])
answer = {}


# Idea is to make it bipertite, we make it so that 1-n are shooter, and when shooter i is target they are i+n
start = 0 # Add source and sink node and add edges between shooters to start and target to sink
sink = 2*n+1
for i in range(n):
    edge_cap[start, i+1] = 1
    edge_cap[i+1+n, sink] = 1
    edges[start].append(i+1)
    edges[i+1+n].append(sink)
    
    

for i in range(m):
    p1, p2 = map(int, sys.stdin.readline().split())
    edge_cap[p1, p2+n] = 1
    edge_cap[p2, p1+n] = 1
    edges[p1].append(p2+n)
    edges[p2].append(p1+n)
    edges[p1+n].append(p2) # Edges back to retrack
    edges[p2+n].append(p1)


def create_path(parent):
    t = sink
    while t != start:
        p = parent[t]
        answer[p] = t
        edge_cap[p, t] -= 1 # for this problem you know the cap is 1 and if it raeches sink it is 1
        edge_cap[t, p] += 1 # allow retrack
        t = p
    return True

    
def bfs():
    q = queue.Queue()
    q.put(start)
    parent = {}
    parent[start] = start
    while not q.empty():
        node = q.get()
        for node2 in edges[node]:
            if node2 in parent: #visited
                continue
            if edge_cap[node, node2] <= 0: # no capacity left
                continue
            parent[node2] = node
            q.put(node2)
            
            if node2 == sink: # reached
                return create_path(parent)
                
            
def karp():
    flow = 0
    while P := bfs():
        flow += 1 # Reached ergo it still has flow of at least 1
    if flow == n: #If all player can shoot/be shot
        for i in range(1, n+1):
            print(answer[i]-n) # -n since target is i+n
    else:
        print("Impossible")

karp()

print(edge_cap)
print(edge_cap[1, 0])