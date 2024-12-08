with open("input.txt", "r") as f:
    data = f.read().split("\n")
# [(0, 5), (2, 6), (3, 9), (4, 2), (6, 3), (8, 4)]

board = set()
store = {}
length = len(data[0])
width = len(data)

for i, line in enumerate(data):
    for j, char in enumerate(line):
        board.add((i, j))
        if char != ".":
            if char in store:
                store[char].append((i, j))
            else:
                store[char] = [(i, j)]

antinode_pos = set()

for v in store.values():
    for i, pos1 in enumerate(v[:-1]):
        for pos2 in v[i + 1 :]:
            y1 = pos1[0] * 2 - pos2[0]
            x1 = pos1[1] * 2 - pos2[1]

            y2 = pos2[0] * 2 - pos1[0]
            x2 = pos2[1] * 2 - pos1[1]

            if (y1, x1) in board:
                antinode_pos.add((y1, x1))

            if (y2, x2) in board:
                antinode_pos.add((y2, x2))

print(len(antinode_pos))

antinode_pos = set()
count = 0

for v in store.values():
    for i, pos1 in enumerate(v[:-1]):
        for pos2 in v[i + 1 :]:
            k = 1
            while True:
                y1 = (pos1[0] - pos2[0]) * k + pos1[0]
                x1 = (pos1[1] - pos2[1]) * k + pos1[1]
                if (y1, x1) in board:
                    antinode_pos.add((y1, x1))
                else:
                    break
                k += 1

            k = 1
            while True:
                y2 = (pos2[0] - pos1[0]) * k + pos2[0]
                x2 = (pos2[1] - pos1[1]) * k + pos2[1]
                if (y2, x2) in board:
                    antinode_pos.add((y2, x2))
                else:
                    break
                k += 1

for v in store.values():
    for pos in v:
        if pos not in antinode_pos:
            count += 1

print(len(antinode_pos) + count)
