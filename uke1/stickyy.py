import sys
a = 0
lines = []
for line in sys.stdin:
    if a == 2:
        break
    lines.append(line.strip())
    a+=1

correct = lines[0]
sticky = lines[1]

i = 0
o = 0
result = ""
while o < len(sticky):
    if correct[i] == sticky[o]:
        i += 1
        o += 1
        if i == len(correct) and o != len(sticky):
            if sticky[o] not in result:
                result += sticky[o]
            break
    else:
        if sticky[o] not in result:
            result += sticky[o]
        o += 1

print(result)