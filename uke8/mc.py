import sys

def is_available(node, node_edges, color, node_colors):
    for neighbour in node_edges[node]:
        if node_colors[neighbour] == color:
            return False
    return True

def paint(node, node_edges, node_colors, max_colors):
    if node == len(node_edges): # When it has given color to all the nodes it is answer
        return True
    for i in range(1, max_colors+1):
        if is_available(node, node_edges, i, node_colors):
            node_colors[node]=i
            if paint(node+1, node_edges, node_colors, max_colors): #Test colors for next node
                return True
            node_colors[node] = 0 # Set back to zero
    return False

def map_coloring(node_edges):
    for i in range(1, 5): # Check from 1 colors to 4 colors
        node_colors = {i:0 for i in range(len(node_edges))}
        node = 0 # Start with first node

        if paint(node,node_edges, node_colors, i): # If solution found print colors
            print(i)
            return
    print("many")



cases = int(sys.stdin.readline())

for _ in range(cases):
    node_edges = {}
    countries, borders = map(int, sys.stdin.readline().split())

    for i in range(countries):
        node_edges[i] = []
    for i in range(borders):
        a, b = map(int, sys.stdin.readline().split())
        node_edges[a].append(b)
        node_edges[b].append(a)
    
    map_coloring(node_edges)
