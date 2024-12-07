with open("input.txt", "r") as f:
    data = f.read().split("\n")

cache = {}
start_pos = None
guard = ""
for i, row in enumerate(data):
    for j, cell in enumerate(row):
        cache[(i, j)] = cell
        if cell in "<>^v":
            start_pos = (i, j)
            guard = cell


def simulate_1(board, gpos, g, store):
    count = 1
    rotations = []
    while 0 <= gpos[0] < len(board) and 0 <= gpos[1] < len(board[0]):
        if g == "^":
            next_pos = (gpos[0] - 1, gpos[1])
            if 0 <= next_pos[0] < len(board) and 0 <= next_pos[1] < len(
                board[0]
            ):
                if store[next_pos] in ".X":
                    if store[next_pos] == ".":
                        count += 1
                    store[gpos] = "X"
                    rotations.append(next_pos)
                    gpos = next_pos
                elif store[next_pos] == "#":
                    g = ">"
            else:
                break
        elif g == ">":
            next_pos = (gpos[0], gpos[1] + 1)
            if 0 <= next_pos[0] < len(board) and 0 <= next_pos[1] < len(
                board[0]
            ):
                if store[next_pos] in ".X":
                    if store[next_pos] == ".":
                        count += 1
                    store[gpos] = "X"
                    rotations.append(next_pos)
                    gpos = next_pos
                elif store[next_pos] == "#":
                    g = "v"
            else:
                break
        elif g == "v":
            next_pos = (gpos[0] + 1, gpos[1])
            if 0 <= next_pos[0] < len(board) and 0 <= next_pos[1] < len(
                board[0]
            ):
                if store[next_pos] in ".X":
                    if store[next_pos] == ".":
                        count += 1
                    store[gpos] = "X"
                    rotations.append(next_pos)
                    gpos = next_pos
                elif store[next_pos] == "#":
                    g = "<"
            else:
                break
        elif g == "<":
            next_pos = (gpos[0], gpos[1] - 1)
            if 0 <= next_pos[0] < len(board) and 0 <= next_pos[1] < len(
                board[0]
            ):
                if store[next_pos] in ".X":
                    if store[next_pos] == ".":
                        count += 1
                    store[gpos] = "X"
                    rotations.append(next_pos)
                    gpos = next_pos
                elif store[next_pos] == "#":
                    g = "^"
            else:
                break
    return count, rotations


ans, new_blocks = simulate_1(data, start_pos, guard, cache)
print(ans)


def simulate(board, start_pos):
    store = {}
    gpos = start_pos
    g = "^"
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            store[(i, j)] = cell

    last_pos = set()
    count = 0
    while 0 <= gpos[0] < len(board) and 0 <= gpos[1] < len(board[0]):
        if g == "^":
            next_pos = (gpos[0] - 1, gpos[1])
            if 0 <= next_pos[0] < len(board) and 0 <= next_pos[1] < len(
                board[0]
            ):
                if store[next_pos] in ".X":
                    if store[next_pos] == ".":
                        count += 1
                    store[gpos] = "X"
                    gpos = next_pos
                elif store[next_pos] == "#":
                    g = ">"
                    action = (g, next_pos)
                    if action in last_pos:
                        return True
                    else:
                        last_pos.add(action)
            else:
                break
        elif g == ">":
            next_pos = (gpos[0], gpos[1] + 1)
            if 0 <= next_pos[0] < len(board) and 0 <= next_pos[1] < len(
                board[0]
            ):
                if store[next_pos] in ".X":
                    if store[next_pos] == ".":
                        count += 1
                    store[gpos] = "X"
                    gpos = next_pos
                elif store[next_pos] == "#":
                    g = "v"
                    action = (g, next_pos)
                    if action in last_pos:
                        return True
                    else:
                        last_pos.add(action)
            else:
                break
        elif g == "v":
            next_pos = (gpos[0] + 1, gpos[1])
            if 0 <= next_pos[0] < len(board) and 0 <= next_pos[1] < len(
                board[0]
            ):
                if store[next_pos] in ".X":
                    if store[next_pos] == ".":
                        count += 1
                    store[gpos] = "X"
                    gpos = next_pos
                elif store[next_pos] == "#":
                    g = "<"
                    action = (g, next_pos)
                    if action in last_pos:
                        return True
                    else:
                        last_pos.add(action)
            else:
                break
        elif g == "<":
            next_pos = (gpos[0], gpos[1] - 1)
            if 0 <= next_pos[0] < len(board) and 0 <= next_pos[1] < len(
                board[0]
            ):
                if store[next_pos] in ".X":
                    if store[next_pos] == ".":
                        count += 1
                    store[gpos] = "X"
                    gpos = next_pos
                elif store[next_pos] == "#":
                    g = "^"
                    action = (g, next_pos)
                    if action in last_pos:
                        return True
                    else:
                        last_pos.add(action)
            else:
                break
    return False


count = 0
for block in set(new_blocks):

    t_board = data[:]
    t_board[block[0]] = (
        t_board[block[0]][: block[1]] + "#" + t_board[block[0]][block[1] + 1 :]
    )
    res = simulate(t_board, start_pos)
    if res:
        count += 1
print(count)
