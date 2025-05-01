import sys
from collections import defaultdict
n, k, r = map(int, sys.stdin.readline().split())
dna = list(map(int, sys.stdin.readline().split()))
req = {}
for i in range(r):
    base, minimum = map(int, sys.stdin.readline().split())
    req[base] = minimum

curr = defaultdict(int) # Current in window
for a in dna:
    curr[a] = 0

best = float("inf") # Smallest window
cur_len = 0 # Current len of window
start = 0 # Start of window
curr_count = 0 # Current 
last_o = 0 # Move start
for i in range(n):
    curr[dna[i]] += 1
    cur_len += 1

    if dna[i] in req and curr.get(dna[i]) == req.get(dna[i]): # ONly if equal since when remove again the others are above
        curr_count += 1 # Update number of satisfied
    if curr_count == r: #check that all satisified
        if best > cur_len:
            best = cur_len
        
        for o in range(start, i, 1):
            last_o = o 
            
            curr[dna[o]] -= 1
            cur_len -= 1
            if dna[o] not in req or req.get(dna[o]) <= curr.get(dna[o]): # Decrese window
                if cur_len < best:
                    best = cur_len 
            else:
                curr_count -= 1 # not longer valid
                break
        
        start = last_o + 1 #update start of window



if best == float("inf"):
    print("impossible")
else:
    print(max(0, best))




