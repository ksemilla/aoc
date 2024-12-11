with open("input.txt", "r") as f:
    nums = f.read()

def recur(num, blinks, store):

    if blinks == 0:
        return 1
    
    if num in store and blinks in store[num]:
        return store[num][blinks]
    
    total = 0
    if num == "0":
        ans = recur("1", blinks - 1, store)
        if num in store:
            store[num][blinks] = ans
        else:
            store[num] = {blinks: ans}
        total += ans
    elif len(num) % 2 == 0:
        ans = recur(str(int(num[:len(num)//2])), blinks - 1, store) + recur(str(int(num[len(num)//2:])), blinks - 1, store)
        if num in store:
            store[num][blinks] = ans
        else:
            store[num] = {blinks: ans}
        total += ans
    else:
        ans = recur(str(int(num) * 2024), blinks - 1, store)
        if num in store:
            store[num][blinks] = ans
        else:
            store[num] = {blinks: ans}
        total += ans

    return total

ans = 0
for num in nums.split(" "):
    ans += recur(num, 25, {})
print(ans)

ans = 0
for num in nums.split(" "):
    ans += recur(num, 75, {})
print(ans)