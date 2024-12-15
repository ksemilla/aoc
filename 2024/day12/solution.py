with open("input.txt", "r") as f:
    data = f.read().split("\n")
length = len(data)
width = len(data[0])
store = {}

for i, row in enumerate(data):
    for j, char in enumerate(row):
        store[(i, j)] = char

visited = set()
areas = []
perimeters = []
sides = []
plants = []
for i, row in enumerate(data):
    for j, char in enumerate(row):
        pos = (i, j)
        if pos not in visited:
            plants.append(store[pos])
            visited.add(pos)
            to_visit = [pos]
            area = { pos }
            perimeter = set()
            v_side = {}
            h_side = {}
            while to_visit:
                next_visit = []
                for next_pos in to_visit:

                    up_pos = (next_pos[0] - 1, next_pos[1])
                    down_pos = (next_pos[0] + 1, next_pos[1])
                    left_pos = (next_pos[0], next_pos[1] - 1)
                    right_pos = (next_pos[0], next_pos[1] + 1)

                    if up_pos not in store or store[up_pos] != store[next_pos]:
                        perimeter.add(("up_pos", up_pos[0], up_pos[1]))
                        h_side[(next_pos[0], next_pos[1], next_pos[1] + 1, "u")] = 1
                    if up_pos in store and up_pos not in visited and store[up_pos] == store[pos]:
                        next_visit.append(up_pos)
                        visited.add(up_pos)
                        area.add(up_pos)
                    
                    if down_pos not in store or store[down_pos] != store[next_pos]:
                        perimeter.add(("down_pos", down_pos[0], down_pos[1]))
                        h_side[(next_pos[0] + 1, next_pos[1], next_pos[1] + 1, "d")] = 1
                    if down_pos in store and down_pos not in visited and store[down_pos] == store[pos]:
                        next_visit.append(down_pos)
                        visited.add(down_pos)
                        area.add(down_pos)

                    if left_pos not in store or store[left_pos] != store[next_pos]:
                        perimeter.add(("left_pos", left_pos[0], left_pos[1]))
                        v_side[(next_pos[1], next_pos[0], next_pos[0] + 1, "l")] = 1
                    if left_pos in store and left_pos not in visited and store[left_pos] == store[pos]:
                        next_visit.append(left_pos)
                        visited.add(left_pos)
                        area.add(left_pos)

                    if right_pos not in store or store[right_pos] != store[next_pos]:
                        perimeter.add(("right_pos", right_pos[0], right_pos[1]))
                        v_side[(next_pos[1] + 1, next_pos[0], next_pos[0] + 1, "r")] = 1
                    if right_pos in store and right_pos not in visited and store[right_pos] == store[pos]:
                        next_visit.append(right_pos)
                        visited.add(right_pos)
                        area.add(right_pos)

                to_visit = next_visit
            areas.append(len(area))
            perimeters.append(len(perimeter))
            while True:
                initial_len = len(v_side)
                l1 = None
                l2 = None
                for line_1 in v_side.keys():
                    for line_2 in v_side.keys():
                        if line_1[0] == line_2[0] and line_1[3] == line_2[3]:
                            if line_1[1] == line_2[2]:
                                l1 = line_1
                                l2 = line_2
                                v_side.pop(l1)
                                v_side.pop(l2)
                                break
                    if l1 and l2:
                        break
                if l1 and l2:
                    v_side[(l1[0], l2[1], l1[2], l1[3])] = 1
                end_len = len(v_side)
                if initial_len == end_len:
                    break
            while True:
                initial_len = len(h_side)
                l1 = None
                l2 = None
                for line_1 in h_side.keys():
                    for line_2 in h_side.keys():
                        if line_1[0] == line_2[0]:
                            if line_1[1] == line_2[2] and line_1[3] == line_2[3]:
                                l1 = line_1
                                l2 = line_2
                                h_side.pop(l1)
                                h_side.pop(l2)
                                break
                    if l1 and l2:
                        break
                if l1 and l2:
                    h_side[(l1[0], l2[1], l1[2], l1[3])] = 1
                end_len = len(h_side)
                if initial_len == end_len:
                    break
            sides.append(len(h_side) + len(v_side))

ans1 = 0
ans2 = 0
for i,area in enumerate(areas):
    ans1 += area * perimeters[i]
    ans2 += area * sides[i]
print(ans1)
print(ans2)