import sys

def trie(words):
    root = {}
    for word in words:
        current = root
        for letter in word:
            current = current.setdefault(letter, {})
        current["*"] = "*"

    return root

def find(t, w):
    count = 0
    current = t
    for letter in w:
        if letter not in current:
            return count
        count += len(current[letter])
        current = current[letter]
    return current

n = int(sys.stdin.readline())
words = []
for i in range(n):
    words.append(sys.stdin.readline().strip())

T = trie(words)

print(T["h"].keys())
m = int(sys.stdin.readline())
for i in range(m):

    print(find(T, sys.stdin.readline().strip()))

