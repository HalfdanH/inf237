import sys
import time


class Node:
    def __init__(self):
        self.count = 1 # Visited once
        self.final = 0 # If end of word it is different then 0 
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

def find(trie_node, word):
    count = trie_node.count
    for letter in word:
        if letter in trie_node.children:
            trie_node = trie_node.children[letter]
            count+= trie_node.count
        else:
            return count-1 
    if trie_node.final == 0: # If not final it does not match
        return count-1
    
    return(trie_node.final-1) #since the root starts with 1 extra
        
n = int(sys.stdin.readline())
words = [0]*n
for i in range(n):
    words[i] = sys.stdin.readline().strip()

T = trie(words)

m = int(sys.stdin.readline())
for i in range(m):

    print(find(T, sys.stdin.readline().strip()))
    