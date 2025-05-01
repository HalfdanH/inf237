import sys
import heapq

# Same idea as nikola, but we need to buil solution after since adding string is O(n)
def build(ex,solution, index):
    height = 0 # Start at height 0 at the end of the workout
    new_sol =[]
    while index > 0:
        new_sol.append(solution[(index, height)])
        if solution[(index, height)] == "D":
            height += ex[index-1] # If we went down, we need to add (opposite of how we got there) the height of the last to get to the next
        else:
            height-= ex[index-1]
        index-=1
    
    a = new_sol[::-1] # Reverse it to get the correct order
    return "".join(a)


def best_exercise(ex, s):
    sol = {} # Solution for each index and heoght, where it went
    n = len(ex)
    heap =[(0, 0, 0)] # Heap sorted by max height
    heapq.heapify(heap)
    while heap:
        max_height, height, index = heapq.heappop(heap)
        if index==n: # If u reach end point end height is 0
            if height == 0:
                return build(ex, sol, index) # First time we reach "correct" end point it is best since heap sorted by max height
            
        else:
            # Down check first
            if height-ex[index] >= 0: # Cant be below 0
                if (index+1, height-ex[index]) not in sol: # If we havent reached yet
                    heapq.heappush(heap, (max_height, height-ex[index], index+1))
                    sol[(index+1, height-ex[index])] = "D" # We went down to get here

            # Up check
            if height+ex[index] <= s: # Cant be higher than sum/2
                if height+ex[index] > max_height:
                    max_height = height+ex[index]
                if (index+1, height+ex[index]) not in sol:
                    heapq.heappush(heap, (max_height, height+ex[index], index+1))
                    sol[(index+1, height+ex[index])] = "U" # We went up to get here
                    

    return "IMPOSSIBLE"    
        


cases = int(sys.stdin.readline())
results = []
for i in range(cases):
    n = int(sys.stdin.readline())
    ex = list(map(int, sys.stdin.readline().split()))
    s = sum(ex)
    if s % 2 != 0:
        results.append("IMPOSSIBLE") # Has to be even since equal up and down
    else:
        results.append(best_exercise(ex, s//2)) # Cant go higher then half the sum

for i in range(cases):
    print(results[i])
