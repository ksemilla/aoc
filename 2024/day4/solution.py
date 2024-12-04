with open("input.txt", "r") as f:
    data = f.read().split("\n")

new_data = []

l = len(data[0])
w = len(data)

ans = 0

for line in data:
    ans += line.count("XMAS") + line[::-1].count("XMAS")
    line = ""
for i in range(l):
    for j in range(w):
        line += data[j][i]
    ans += line.count("XMAS") + line[::-1].count("XMAS")
for j in range(w)[::-1]:
    start_j = j
    start_i = 0
    while 0 <= start_i < l and 0 <= start_j < w:
        line += data[start_j][start_i]
        start_i += 1
        start_j += 1
    line = ""
for i in range(1, l):
    start_j = 0
    start_i = i
    while 0 <= start_i < l and 0 <= start_j < w:
        line += data[start_j][start_i]
        start_i += 1
        start_j += 1
    ans += line.count("XMAS") + line[::-1].count("XMAS")
    line = ""
for i in range(l):
    start_i = i
    start_j = 0
    while 0 <= start_i < l and 0 <= start_j < w:
        line += data[start_j][start_i]
        start_i -= 1
        start_j += 1
    ans += line.count("XMAS") + line[::-1].count("XMAS")
    line = ""
for j in range(1, w):
    start_i = l - 1
    start_j = j
    while 0 <= start_i < l and 0 <= start_j < w:
        line += data[start_j][start_i]
        start_i -= 1
        start_j += 1
    ans += line.count("XMAS") + line[::-1].count("XMAS")
    line = ""
print(ans)

ans = 0

for j in range(1, w - 1):
    for i in range(1, l - 1):
        if data[j][i] == "A":
            if (
                data[j - 1][i - 1] == "M"
                and data[j + 1][i + 1] == "S"
                and data[j + 1][i - 1] == "M"
                and data[j - 1][i + 1] == "S"
            ):
                ans += 1
                continue
            elif (
                data[j + 1][i - 1] == "M"
                and data[j - 1][i + 1] == "S"
                and data[j + 1][i + 1] == "M"
                and data[j - 1][i - 1] == "S"
            ):
                ans += 1
                continue
            elif (
                data[j + 1][i + 1] == "M"
                and data[j - 1][i - 1] == "S"
                and data[j - 1][i + 1] == "M"
                and data[j + 1][i - 1] == "S"
            ):
                ans += 1
                continue
            elif (
                data[j - 1][i - 1] == "M"
                and data[j + 1][i + 1] == "S"
                and data[j - 1][i + 1] == "M"
                and data[j + 1][i - 1] == "S"
            ):
                ans += 1
                continue

print(ans)
