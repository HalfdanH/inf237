import sys

name = sys.stdin.readline()
name_list = name.split(sep="-")
out = ""
for name in name_list:
    out = out + name[0]
    
print(out)