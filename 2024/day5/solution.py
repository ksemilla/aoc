with open("input.txt", "r") as f:
    rules, updates = [x.split("\n") for x in f.read().split("\n\n")]

store = {}
ans = 0
invalids = []
for x in rules:
    l, r = x.split("|")
    if l in store:
        store[l].add(r)
    else:
        store[l] = {r}

for line in updates:
    valid = True
    line = line.split(",")
    for i, num in enumerate(line):
        for j in range(i - 1, -1, -1):
            if num in store and line[j] in store[num]:
                valid = False
                invalids.append(line)
                break
        if not valid:
            break

    if valid:
        ans += int(line[len(line) // 2])

print(ans)

ans = 0
for line in invalids:
    while True:
        for rule in rules:
            l, r = rule.split("|")
            if l in line and r in line:
                li = line.index(l)
                ri = line.index(r)
                if ri < li:
                    line[::] = line[:ri] + [l] + line[ri:]
                    line.pop(li + 1)
                    break
        else:
            break
    ans += int(line[len(line) // 2])
print(ans)
