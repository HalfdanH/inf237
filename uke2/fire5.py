import sys
import queue
import copy
import time

import time

start_time = time.time()

def spread_fire(field,fireq):
    time = {}
    new_fire_q = queue.Queue()
    while not fireq.empty():
        pos = fireq.get()
        time[pos] = 1
        new_fire_q.put(pos)
    fireq = new_fire_q

    while not fireq.empty():
        pos = fireq.get()
        
        for i in range(pos[0]-1, pos[0]+2, 2):
            try:
                if field[i][pos[1]] == "." or field[i][pos[1]] == "@":
                    new_pos = (i, pos[1])
                    fireq.put(new_pos)
                    field[i][pos[1]] = "*"
                    time[new_pos] = time[pos] + 1
            except:
                pass
        
        for i in range(pos[1]-1, pos[1]+2, 2):
            try:
                if field[pos[0]][i] == "." or field[pos[0]][i] == "@":
                    new_pos = (pos[0], i)
                    fireq.put(new_pos)
                    field[pos[0]][i] = "*"
                    time[new_pos] = time[pos] + 1
            except:
                pass

            
    return time   

        
        
        

def bfs(field, height, width, q, fireq):
    fieldc = copy.deepcopy(field)
    fire_time = spread_fire(fieldc, fireq)
    time = {}
    pos = q.get()
    field[pos[0]][pos[1]] = "+"
    time[pos] = 1
    q.put(pos)
    while not q.empty():
        pos = q.get()

        if pos[0] == height-1 or pos[0] == 0:
            return time[pos]
        
        if pos[1] == width-1 or pos[1] == 0:
            return time[pos]
        for i in range(pos[0]-1, pos[0]+2, 2):
            try:
                new_pos = (i, pos[1])
                time[new_pos] = time[pos] + 1
                if field[i][pos[1]] == "." and (fire_time.get(new_pos) is None or fire_time[new_pos] > time[new_pos]):
                    q.put(new_pos)
                    field[i][pos[1]] = "+"
                
            except:
                pass
        
        for i in range(pos[1]-1, pos[1]+2, 2):
            try:
                new_pos = (pos[0], i)
                time[new_pos] = time[pos] + 1
                if field[pos[0]][i] == "." and (fire_time.get(new_pos) is None or fire_time[new_pos] > time[new_pos]):
                    q.put(new_pos)
                    field[pos[0]][i] = "+"
            except:
                pass

            
    return "Impossible"


n_cases = int(sys.stdin.readline())             
result = []
for i in range(n_cases): #Fix after
    width, height = map(int, sys.stdin.readline().split())
    field = []
    fireq = queue.Queue()
    q = queue.Queue()
    for h in range(height):
        row = list(sys.stdin.readline().strip())
        for w in range(width):
            if row[w] == "@":
                q.put((h, w))
            elif row[w] == "*":
                fireq.put((h, w))
        field.append(row)
    results = str(bfs(field, height, width, q, fireq))
    result.append(results)


print("\n".join(result))

end_time = time.time()

print("Execution Time:", end_time - start_time, "seconds")