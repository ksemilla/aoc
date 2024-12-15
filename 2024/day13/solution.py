with open("input.txt", "r") as f:
    data = f.read().split("\n\n")

final_total = 0
for block in data:
    button_a, button_b, prize = block.split("\n")
    _, _, button_a_x, button_a_y = button_a.split(" ")
    _, _, button_b_x, button_b_y = button_b.split(" ")
    button_a_x = int(button_a_x[2:-1])
    button_a_y = int(button_a_y[2:])
    button_b_x = int(button_b_x[2:-1])
    button_b_y = int(button_b_y[2:])
    _, prize_x, prize_y = prize.split(" ")
    prize_x = int(prize_x[2:-1])
    prize_y = int(prize_y[2:])
    max_x = prize_x // button_a_x + 1
    total_tokens = None
    for clicks_a in range(1, max_x + 1):
        weight_a_x = button_a_x * clicks_a
        weight_a_y = button_a_y * clicks_a

        clicks_b = (prize_x - weight_a_x) // button_b_x
        if clicks_b > -1:
            res_x = button_a_x * clicks_a + button_b_x * clicks_b
            res_y = button_a_y * clicks_a + button_b_y * clicks_b
            if prize_x == res_x and prize_y == res_y:
                total = clicks_a * 3 + clicks_b
                if not total_tokens:
                    total_tokens = total
                elif total_tokens > total:
                    total_tokens = total
    if total_tokens:
        final_total += total_tokens

print(final_total)

total = 0
for block in data:
    button_a, button_b, prize = block.split("\n")
    _, _, button_a_x, button_a_y = button_a.split(" ")
    a1 = int(button_a_x[2:-1])
    a2 = int(button_a_y[2:])

    _, _, button_b_x, button_b_y = button_b.split(" ")
    b1 = int(button_b_x[2:-1])
    b2 = int(button_b_y[2:])

    _, prize_x, prize_y = prize.split(" ")
    c1 = int(prize_x[2:-1]) + 10000000000000
    c2 = int(prize_y[2:]) + 10000000000000
    y = (a1 * c2 - a2 * c1) // (a1 * b2 - a2 * b1)
    x = (c1 - b1 * y) // a1
    if a1 * x + b1 * y == c1 and a2 * x + b2 * y == c2:
        total += x * 3 + y

print(total)
