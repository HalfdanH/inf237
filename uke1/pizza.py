import sys

crust_pizza = sys.stdin.readline().strip().split(sep=" ")

pizza = int(crust_pizza[0])
crust = int(crust_pizza[1])
cheese = pizza-crust
print((cheese**2/pizza**2)*100)