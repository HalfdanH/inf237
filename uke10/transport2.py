import sys
import queue
from collections import defaultdict

edges = defaultdict(lambda: [])
edge_cap = defaultdict(lambda: 0)
n, r, f, t = map(int, sys.stdin.readline().split())

SINK = n+2*t+1
START = 0

material = sys.stdin.readline().split()
material_set = set()
factories = sys.stdin.readline().split()
factories_set = set()

to_int = {} # Convert names to ints for faster comparison
curr = 1 
for node in material: # Edges from source to material
    edges[START].append(curr) #
    edge_cap[START, curr] = 1
    material_set.add(curr)
    to_int[node] = curr
    curr += 1

for node in factories: # Edges from factories to sink
    edges[curr].append(SINK)
    edge_cap[curr, SINK] = 1
    factories_set.add(curr)
    to_int[node] = curr
    curr+=1

for _ in range(t):
    to_transport = curr
    curr += 1
    transport_to = curr
    curr += 1
    edges[to_transport].append(transport_to)
    edges[transport_to].append(to_transport)
    edge_cap[to_transport, transport_to] = 1 # Only allow company to provide 1 to where they shall

    data = sys.stdin.readline().split()
    nr = int(data[0])
    for i in range(1, nr+1):
        if data[i] not in to_int:
            to_int[data[i]] = curr
            curr += 1
        node = to_int[data[i]]
        if node in material_set: # Company can get material
            edges[node].append(to_transport)
            edges[to_transport].append(node) # Allow retrack
            edge_cap[node, to_transport] = 1
        elif node in factories_set: # Can send to factroy
            edges[node].append(transport_to)
            edges[transport_to].append(node)        
            edge_cap[transport_to, node] = 1
        else: # Nodes in middle can get and give to transport
            edges[node].append(to_transport)
            edges[to_transport].append(node)
            edge_cap[node, to_transport] = 1

            edges[node].append(transport_to)
            edges[transport_to].append(node)        
            edge_cap[transport_to, node] = 1


def create_path(parent):
    node = SINK
    path = [node]
    while node != START:
        node = parent[node]
        path.append(node)
    return tuple(reversed(path))

def bfs(start, target):
    q = queue.Queue()
    q.put(start)
    parent = {start: start}
    while not q.empty():
        node = q.get()
        for neigh in edges[node]:
            if neigh in parent or edge_cap[node, neigh] <= 0:
                continue
            parent[neigh] = node
            q.put(neigh)
            if neigh == target:
                return create_path(parent)
    
edge_funx = lambda p: zip(p, p[1:])
def edmond():
    flow = 0
    while P:= bfs(START, SINK):
        flow += 1
        for i in range(1, len(P)):
            u, v = P[i-1], P[i]
            edge_cap[u, v] -= 1
            edge_cap[v, u] += 1
    print(flow)

    
edmond()

print(edge_cap)
print(edge_cap[1, 0])
