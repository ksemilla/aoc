with open("input.txt", "r") as f:
    data = f.read().split("\n")


def get_safety(nums):
    if nums[1] > nums[0]:
        is_inc = True
    elif nums[1] < nums[0]:
        is_inc = False
    else:
        return False

    for i, n in enumerate(nums[:-1]):
        res = nums[i + 1] - n
        if res == 0:
            return False
        elif 1 <= res <= 3:
            if not is_inc:
                return False
        elif -3 <= res <= -1:
            if is_inc:
                return False
        else:
            return False

    return True


ans = 0

for report in data:

    nums = [int(n) for n in report.split(" ")]
    res = get_safety(nums)

    if res:
        ans += 1
    else:
        for i in range(len(nums)):
            res = get_safety(nums[:i] + nums[i + 1 :])
            if res:
                # print(nums, i)
                ans += 1
                break

print(ans)
