import sys

def check_row(row, n, holes, cols, top_down,bottom_up):
    total=0
    if row == n:
        return 1 #If all are filled, add 1 to the last total
    
    for col in range(n): #Check all columns
        if col in cols or row-col in top_down or row+col in bottom_up or (row, col) in holes: #Not valid pos
            continue
        cols.add(col) #Column occupied
        top_down.add(row-col) # Diagonal from left top_down taken
        bottom_up.add(row+col) # Diagonal from left down_up taken
        total += check_row(row+1, n, holes, cols, top_down, bottom_up) # Go to next row
        cols.remove(col) #Clear for next
        top_down.remove(row-col)
        bottom_up.remove(row+col)

    return total


def n_queens(n, holes):
    count = check_row(0 ,n, holes, set(), set(), set())
    print(count)

while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break

    holes = set()
    for i in range(M):
        x, y = map(int, sys.stdin.readline().split())
        holes.add((x,y))
    
    n_queens(N, holes)


    