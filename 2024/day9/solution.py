with open("input.txt", "r") as f:
    data = f.read()

disk = []

toggle = 1
j = 0
for i, n in enumerate(data):
    for _ in range(int(n)):
        if toggle == 1:
            disk.append(j)

        else:
            disk.append(".")
    if toggle == 1:
        j += 1
    toggle *= -1

# print("".join(disk))

for i, num in enumerate(disk):
    while disk[-1] == ".":
        disk[:] = disk[:-1]
    if num == ".":
        disk[i] = disk.pop(-1)

ans = 0
for i, n in enumerate(disk):
    ans += i * n
print(ans)

with open("input.txt", "r") as f:
    data = f.read()

disk = []

toggle = 1
j = 0
last_num = -1
for i, n in enumerate(data):
    if toggle == 1:
        last_num = j
        disk.append((j, int(n)))
    else:
        disk.append((-1, int(n)))
    if toggle == 1:
        j += 1
    toggle *= -1

k = 0
while k != last_num:
    block_i = None
    i = len(disk)
    for block in disk[::-1]:
        if block[0] == last_num:
            block_i = i - 1
            break
        i -= 1

    space_i = None
    for l, block in enumerate(disk[:block_i]):
        if block[0] == -1 and block[1] >= disk[block_i][1]:
            space_i = l
            break

    if space_i:
        diff = disk[space_i][1] - disk[block_i][1]
        block = disk[block_i]
        disk[block_i] = (-1, block[1])
        disk = disk[:space_i] + [block] + [(-1, diff)] + disk[space_i + 1 :]

    last_num -= 1

string = []
for n in disk:
    for _ in range(n[1]):
        if n[0] == -1:
            string.append(".")
        else:
            string.append(n[0])
# print(string)

ans = 0

for i, n in enumerate(string):
    if n != ".":
        ans += i * int(n)

print(ans)

# 85937815618 low
# 6389911791746
