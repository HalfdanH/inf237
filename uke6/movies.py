import sys

# Sum segment trees
# Representer tree
# Initialiser filmer som 1 og deretter querys som 0
# Topp er i n - 1 så start 1 1 1(topp) 0 0 0 så reverest og så
# Ha index til filmer i stacken i starten
# Query fra index til høyeste index
# Oppdater boken sin index til høyeste + 1
# Flyy over så start med 3 2 1 
# Start film 
# Query fra index +1 til høyeste index
# Høyeste + 1 index blir 1
# Index blir 0

left = lambda i: 2 * i
right = lambda i: 2 * i + 1
parent = lambda i: i // 2
index = lambda T, i: len(T) // 2 + i

def fill_tree(tree, op=sum):
    internal = range(1, len(tree) // 2)
    for i in reversed(internal):
        tree[i] = op((tree[left(i)], tree[right(i)]))

def update(tree, idx, value, op=sum):
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


cases = int(sys.stdin.readline())

for _ in range(cases):
    result = []
    n_books, n_queries = map(int, sys.stdin.readline().split())
    book_pos = {}
    for i in range(n_books):
        book_pos[i+1] = n_books-(i+1) # Movie 1 at the top, ergo rightmost pos
    highest = n_books-1
    queries = list(map(int, sys.stdin.readline().split()))
    tree = [0] * (n_books+n_queries) + [1] * n_books + [0] * n_queries
    fill_tree(tree)
    for book in queries:
        update(tree, book_pos[book], 0) # Remove book
        highest+=1
        result.append(str(query(tree, book_pos[book], highest)))
        book_pos[book] = highest
        update(tree, highest, 1) # Move movie to the highest (rightmost) pos
    print(" ".join(result))


