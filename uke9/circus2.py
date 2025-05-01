import sys

class Node:
    def __init__(self,number, cost, children):
        self.children = children
        self.parent = -1
        self.cost = cost
        self.number = number

nodes = []
n = int(sys.stdin.readline())
for i in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    node = Node(i,data[0], data[2:2+data[1]])
    nodes.append(node)

for node in nodes:
    for child in node.children:
        nodes[child].parent = node
    
for node in nodes:
    if node.parent == -1: # Find root
        root = node


dp = {} # 

def promote(u):
    return max(0, dp[u][0]-dp[u][1])
    

def dfs(node):
    pick = node.cost
    skip_up = 0
    skip_down = float("inf")
    if len(node.children) == 0: # If leaf
        dp[node.number] = (pick, skip_down, skip_up)
        return

    for c in node.children: # Dfs
        child = nodes[c]
        dfs(child)
        pick += dp[c][2] # If u pick, you have to skip up 
        skip_up += min(dp[c][0], dp[c][1]) # if skip up, pick smallest of pciking children or skipping down
    
    
    skip_down = 0
    p = float("inf")
    for c in node.children:
        skip_down += min(dp[c][0], dp[c][1])
        if promote(c) < p:
            p = promote(c)
        
    skip_down += p
    dp[node.number] = (pick, skip_down, skip_up)


dfs(root)
print(min(dp[root.number][0], dp[root.number][1]))


