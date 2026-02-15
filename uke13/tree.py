import sys
sys.setrecursionlimit(3000)

class Node:
    def __init__(self, parent, depth):
        self.children  = {}
        self.depth = depth
        self.parent = parent
        self.jump = [None]*18

def trie(words):
    root = Node(None, 0)

    word_end = []
    for word in words:
        current = root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = Node(current, current.depth +1)
                current = current.children[letter]
            else:
                current = current.children[letter]
        word_end.append(current)

    return root, word_end




pokemons = []

n, q = map(int, sys.stdin.readline().split())

for i in range(n):
    pokemons.append(sys.stdin.readline().strip())


T, word_end = trie(pokemons)

def build_table(node):
    stack = [node]
    while stack:
        node = stack.pop()
        if node.parent:
            node.jump[0] = node.parent
            for i in range(1, 18):
                curr = node.jump[i-1]
                if curr and curr.jump[i-1]:
                    node.jump[i] = curr.jump[i-1]
        for child in node.children.values():
            stack.append(child)
        
build_table(T)

cache = {}
def cached_lca(node1, node2):
    key = (id(node1), id(node2)) if id(node1) <= id(node2) else (id(node2), id(node1))
    if key not in cache:
        cache[key] = lca(node1, node2)
    return cache[key]
def lca(node1, node2):
    if node1.depth < node2.depth:
        node1, node2 = node2, node1

    for i in reversed(range(18)):
        if node1.jump[i] and node1.jump[i].depth >= node2.depth:
            node1 = node1.jump[i]
    if node1 == node2:
        return node1


    for i in reversed(range(18)):
        if node1.jump[i] and node2.jump[i] and node1.jump[i] != node2.jump[i]:
            node1 = node1.jump[i]
            node2 = node2.jump[i]
    return node1.parent


for _ in range(q):
    total = 0
    k, l = map(int, sys.stdin.readline().split())
    
    his_pokemons = list(map(lambda x: int(x)-1, sys.stdin.readline().split()))

    his_pokemons = [(pokemons[i], i) for i in his_pokemons]
    his_pokemons.sort()
    indexes = [i for _, i in his_pokemons]
    selected = [word_end[i] for i in indexes]
    for j in range(k-l+1):
    
        p1 = selected[j]
        p2 = selected[j+l-1]

        lca_m = lca(p1, p2)
        
        lca_l = None

        if j > 0:
            lca_l = lca(lca_m,selected[j-1])
        if j+l < k:
            lca_r = lca(lca_m, selected[j+l])
            if not lca_l or lca_r.depth > lca_l.depth:
                lca_l = lca_r
    
        if not lca_l:
            total+= lca_m.depth
        else:
            total += lca_m.depth - lca_l.depth
    print(total)