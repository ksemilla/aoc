with open("input.txt", "r") as f:
    data = f.read().splitlines()

store = {}

robots = []

for robot in data:
    pos, velocity = robot.split(" ")
    pos = tuple(int(n) for n in pos[2:].split(","))
    velocity = tuple(int(n) for n in velocity[2:].split(","))
    robots.append({"pos": pos, "velocity": velocity})

width = 101
length = 103

x_axis = length // 2
y_axis = width // 2

for _ in range(100):
    for i, robot in enumerate(robots):
        x = robot["pos"][0] + robot["velocity"][0]

        if x >= width or x < 0:
            x = x % width

        y = robot["pos"][1] + robot["velocity"][1]

        if y >= length or y < 0:
            y = y % length

        robots[i] = {
            "pos": (x, y),
            "velocity": robot["velocity"],
        }

q1 = 0
q2 = 0
q3 = 0
q4 = 0
for robot in robots:
    if robot["pos"][0] < y_axis:
        if robot["pos"][1] < x_axis:
            q1 += 1
        elif robot["pos"][1] > x_axis:
            q3 += 1
    elif robot["pos"][0] > y_axis:
        if robot["pos"][1] < x_axis:
            q2 += 1
        elif robot["pos"][1] > x_axis:
            q4 += 1

print(q1 * q2 * q3 * q4)

# TOO LOW 87904138
import time

with open("input.txt", "r") as f:
    data = f.read().splitlines()

store = {}

robots = []

for robot in data:
    pos, velocity = robot.split(" ")
    pos = tuple(int(n) for n in pos[2:].split(","))
    velocity = tuple(int(n) for n in velocity[2:].split(","))
    robots.append({"pos": pos, "velocity": velocity})

width = 101
length = 103

for k in range(1, 7345):
    for i, robot in enumerate(robots):
        x = robot["pos"][0] + robot["velocity"][0]

        if x >= width or x < 0:
            x = x % width

        y = robot["pos"][1] + robot["velocity"][1]

        if y >= length or y < 0:
            y = y % length

        robots[i] = {
            "pos": (x, y),
            "velocity": robot["velocity"],
        }


store = set()
for robot in robots:
    store.add(robot["pos"])

for i in range(length):
    row = []
    for j in range(width):
        if (j, i) in store:
            row.append("#")
        else:
            row.append(".")
    print("".join(row))
print(k)
