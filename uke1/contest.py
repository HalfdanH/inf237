problems, solved = map(int, input().split())
difficulty, solved_difficulty = map(int, input().split())

x = (difficulty*problems-solved*solved_difficulty)/(problems-solved)

if x > 100 or x < 0:
    print("impossible")
else:
    print(x)