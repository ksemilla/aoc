with open("input.txt", "r") as f:
    data = f.read().split("\n\n")

total = 0
totals = []

for x in data:
    add = sum([int(y) for y in x.split("\n")])
    if add > total:
        total = add
    totals.append(add)

totals.sort()
print(total)
print(sum(totals[-3:]))