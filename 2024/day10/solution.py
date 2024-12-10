with open("input.txt", "r") as f:
    data = f.read().split("\n")

store = {}

trailheads = []

for i, line in enumerate(data):
    for j, char in enumerate(line):
        store[(i, j)] = int(char)
        if int(char) == 0:
            trailheads.append((i, j))
count = 0
for trailhead in trailheads:
    # print(trailhead)
    _to_visit = [trailhead]
    visited = set()
    peaks = set()
    while _to_visit:
        to_visit = _to_visit[:]
        _to_visit = []
        for pos in to_visit:
            visited.add(pos)
            if store[pos] == 9:
                peaks.add(pos)
            if (
                (pos[0] - 1, pos[1]) in store
                and store[(pos[0] - 1, pos[1])] - 1 == store[pos]
                and (pos[0] - 1, pos[1]) not in visited
            ):
                _to_visit.append((pos[0] - 1, pos[1]))
            if (
                (pos[0] + 1, pos[1]) in store
                and store[(pos[0] + 1, pos[1])] - 1 == store[pos]
                and (pos[0] + 1, pos[1]) not in visited
            ):
                _to_visit.append((pos[0] + 1, pos[1]))
            if (
                (pos[0], pos[1] + 1) in store
                and store[(pos[0], pos[1] + 1)] - 1 == store[pos]
                and (pos[0], pos[1] + 1) not in visited
            ):
                _to_visit.append((pos[0], pos[1] + 1))
            if (
                (pos[0], pos[1] - 1) in store
                and store[(pos[0], pos[1] - 1)] - 1 == store[pos]
                and (pos[0], pos[1] - 1) not in visited
            ):
                _to_visit.append((pos[0], pos[1] - 1))

    #     print(_to_visit)
    # print("-------------------------------")
    count += len(peaks)

print(count)

with open("input.txt", "r") as f:
    data = f.read().split("\n")

store = {}

trailheads = []

for i, line in enumerate(data):
    for j, char in enumerate(line):
        store[(i, j)] = int(char)
        if int(char) == 0:
            trailheads.append((i, j))
count = 0
for trailhead in trailheads:
    # print(trailhead)
    _to_visit = [trailhead]
    visited = set()
    peaks = set()
    while _to_visit:
        to_visit = _to_visit[:]
        _to_visit = []
        for pos in to_visit:
            visited.add(pos)
            if store[pos] == 9:
                count += 1
            if (
                (pos[0] - 1, pos[1]) in store
                and store[(pos[0] - 1, pos[1])] - 1 == store[pos]
                and (pos[0] - 1, pos[1]) not in visited
            ):
                _to_visit.append((pos[0] - 1, pos[1]))
            if (
                (pos[0] + 1, pos[1]) in store
                and store[(pos[0] + 1, pos[1])] - 1 == store[pos]
                and (pos[0] + 1, pos[1]) not in visited
            ):
                _to_visit.append((pos[0] + 1, pos[1]))
            if (
                (pos[0], pos[1] + 1) in store
                and store[(pos[0], pos[1] + 1)] - 1 == store[pos]
                and (pos[0], pos[1] + 1) not in visited
            ):
                _to_visit.append((pos[0], pos[1] + 1))
            if (
                (pos[0], pos[1] - 1) in store
                and store[(pos[0], pos[1] - 1)] - 1 == store[pos]
                and (pos[0], pos[1] - 1) not in visited
            ):
                _to_visit.append((pos[0], pos[1] - 1))

    #     print(_to_visit)
    # print("-------------------------------")
    # count += len(peaks)

print(count)
