n, m = map(int, input().split())
fishes = list(map(int, input().split()))
mongers = [tuple(map(int, input().split())) for _ in range(m)]


fishes = sorted(fishes)
mongers = sorted(mongers, key=lambda x:x[1])
monitos = 0

while fishes and mongers:
    i = mongers[len(mongers)-1][0]
    while i > 0:
        monitos += fishes[len(fishes)-1]*mongers[len(mongers)-1][1]
        fishes.pop()
        i-= 1
        if not fishes:# or not mongers:
            break
    mongers.pop()     

print(monitos)