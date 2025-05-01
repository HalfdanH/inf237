import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

smallest = deque()
biggest = deque() # double edge que to remove from both left and right fast
curr = float("inf")
for i in range(n):

    if len(smallest) != 0 and smallest[0] < i-k+1:
        smallest.popleft() # Pop if out of window

    if len(biggest) != 0 and biggest[0] < i-k+1:
        biggest.popleft()


    while len(smallest) != 0 and trees[i] < trees[smallest[-1]]:
        smallest.pop() # Pop trees bigger than new

    smallest.append(i) # Save index


    while len(biggest) != 0 and trees[i] > trees[biggest[-1]]: 
        biggest.pop() # Pop trees smaller than new
    biggest.append(i) #Save index

    if i >= k-1: # only check after valid amount of trees
        if trees[biggest[0]] - trees[smallest[0]] < curr:
            curr = trees[biggest[0]] - trees[smallest[0]]


    
print(curr)