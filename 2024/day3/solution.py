with open("input.txt", "r") as f:
    data = f.read()

ans = 0
i = 0
length = len(data)

found_start = False
found_comma = False

do = True

x_str = ""
y_str = ""
while i < length:
    if data[i : i + 4] == "do()":
        do = True
        i += 4
    elif data[i : i + 7] == "don't()":
        do = False
        i += 7
    elif data[i : i + 4] == "mul(":
        found_start = True
        i += 4
    elif found_start:
        if data[i] in "1234567890":
            x_str += data[i]
        elif data[i] == ",":
            found_comma = True
            found_start = False
        else:
            found_start = False
            found_comma = False
            x_str = ""
            y_str = ""
        i += 1
    elif found_comma:
        if data[i] in "1234567890":
            y_str += data[i]
        elif data[i] == ")":
            if do:
                ans += int(x_str) * int(y_str)

            found_start = False
            found_comma = False
            x_str = ""
            y_str = ""
        else:
            found_start = False
            found_comma = False
            x_str = ""
            y_str = ""
        i += 1
    else:
        found_start = False
        found_comma = False
        x_str = ""
        y_str = ""
        i += 1

print(ans)
