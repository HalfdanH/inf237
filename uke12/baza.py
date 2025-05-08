import sys
import time


class Node:
    def __init__(self):
        self.count = 1 # Visited once
        self.final = 0 # If 
        self.children  = {}

def trie(words):
    root = Node()
    for word in words:
        root.count+=1
        current = root
        count = root.count
        for letter in word:
            if letter not in current.children:
                current.children[letter] = Node()
                current = current.children[letter]
                count+=1
            else:
                current = current.children[letter]
                current.count += 1
                count+= current.count

        current.final = count


    return root

def find(t, w):
    count = t.count
    for letter in w:
        if letter in t.children:
            t = t.children[letter]
            count+= t.count
        else:
            return count-1
    if t.final == 0: # If not final it does not match
        return count-1
    
    return(t.final-1)
        
n = int(sys.stdin.readline())
words = [0]*n
for i in range(n):
    words[i] = sys.stdin.readline().strip()

T = trie(words)

m = int(sys.stdin.readline())
for i in range(m):

    print(find(T, sys.stdin.readline().strip()))
    