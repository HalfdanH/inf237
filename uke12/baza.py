import sys
import time

s = time.time()
def trie(words):
    root = {0: 0, 1:0}
    for word in words:
        root[0]+=1
        current = root
        count = root[0]
        for letter in word:
            if letter not in current:
                current[letter] = {0: 1, 1: 0}
                current = current[letter]
                count+=1
            else:
                current = current[letter]
                current[0] += 1
                count+= current[0]

        current[1] = count
        #current["*"] = "*"


    return root

def find(t, w):
    count = t[0]
    for letter in w:
        if letter in t:
            t = t[letter]
            count+= t[0]
        else:
            return count
    if t[1] == 0:
        return count
    
    return(t[1])
        


n = int(sys.stdin.readline())
words = [0]*n
for i in range(n):
    words[i] = sys.stdin.readline().strip()

T = trie(words)

m = int(sys.stdin.readline())
for i in range(m):

    print(find(T, sys.stdin.readline().strip()))
    

e = time.time()
#print((e-s))