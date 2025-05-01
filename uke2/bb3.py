import sys
import queue

nodes = set()
edges = {}
switch = {"jesse": "walter", "walter": "jesse"}
assigned = {}
n = int(sys.stdin.readline())
for _ in range(n):
    item = sys.stdin.readline().strip()
    nodes.add(item)
    edges[item] = set()  

m = int(sys.stdin.readline())
for _ in range(m):
    item1, item2 = sys.stdin.readline().strip().split()   
    edges[item1].add(item2)
    edges[item2].add(item1)


def bfs(item):
    q = queue.Queue()
    curr = "walter"
    q.put(item)
    assigned[item] = curr
    while not q.empty():
        item = q.get()
        curr = switch[assigned[item]]
        for n in edges[item]:
            if n in assigned.keys():
                if assigned[n] != curr:
                    return "impossible"
            else:
                assigned[n] = curr
                q.put(n)


for item in nodes:
    if item not in assigned.keys():  
        a = bfs(item)
        if a == "impossible":
            break

jesse = []
walter = []
if a == "impossible":
    print(a)
else:
    for item in nodes:
        if assigned[item] == "walter":
            walter.append(item)
        else:
            jesse.append(item)
    print(" ".join(walter).strip())
    print(" ".join(jesse).strip())