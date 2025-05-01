import sys
# Initiliser med enere
# For posisjon i orginalliste
# Start med L = 1 og R = N
# Finn index til 1
# IKkke ta med Først posisjon så sjekk hvor du kommer fra
# Query
# Key er tallet og index som verdi
# Hvor er tall 1: 4
# Opdatere treet, sett 4 i 0
# SÅ query
# Bruke sum
# Query annenhver gang med L og R
# Query hele veien ut

# Starter med L og R og start 1 ere i treet
# Opdater posijon i tre til 0, gå fra venstre til posisjon
# Så R og sjekker N

n = int(sys.stdin.readline())
data = {}
for i in range(n):
    data[int(sys.stdin.readline())] = i
    

tree = [0] * len(data) + [1]* len(data)
left = lambda i: 2 * i
right = lambda i: 2 * i + 1
parent = lambda i: i // 2
index = lambda T, i: len(T) // 2 + i

def fill_tree(tree, op=sum):
    internal = range(1, len(tree) // 2)
    for i in reversed(internal):
        tree[i] = op((tree[left(i)], tree[right(i)]))

def update_pos(tree, idx, value, op=sum):
    idx = index(tree, idx)
    tree[idx] = value
    while (idx := parent(idx)) > 0:
        tree[idx] = op((tree[left(idx)], tree[right(idx)]))


def q(T, l, r):
    yield T[l]
    while True:
        pl = parent(l)
        pr = parent(r)
        if pl == pr:
            return
        if l % 2 == 0:
            yield T[right(pl)]
        
        if r % 2 == 1:
            yield T[left(pr)]
        l = pl
        r = pr

def query(T, l, r, op=sum):
    l = index(T, l)
    r = index(T, r)
    return op(q(T, l, r))

fill_tree(tree)

l = 1
r = n
for i in range(n):
    if i % 2 == 0: # Every other from right to left
        left_index = data[l]
        update_pos(tree, left_index, 0) # Number is moved out to the side so it isnt "in the list"
        print(query(tree, 0, left_index))
        l += 1
    else:
        right_index = data[r]
        update_pos(tree, right_index, 0)
        print(query(tree, right_index, n))
        r -= 1


