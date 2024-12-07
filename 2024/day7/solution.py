with open("input.txt", "r") as f:
    data = f.read().split("\n")


def recur(target, acc, nums):
    if not nums:
        if target == acc:
            return True
        return False

    res_1 = acc + nums[0]
    res_2 = acc * nums[0]
    return any([recur(target, res_1, nums[1:]), recur(target, res_2, nums[1:])])


ans = 0
for line in data:
    target, nums = line.split(": ")
    target = int(target)
    nums = [int(n) for n in nums.split(" ")]
    res = recur(target, nums[0], nums[1:])
    if res:
        ans += target
print(ans)


def recur_2(target, acc, nums):
    if not nums:
        if target == acc:
            return True
        return False

    res_1 = acc + nums[0]
    res_2 = acc * nums[0]
    res_3 = int(str(acc) + str(nums[0]))
    return any(
        [
            recur_2(target, res_1, nums[1:]),
            recur_2(target, res_2, nums[1:]),
            recur_2(target, res_3, nums[1:]),
        ]
    )


ans = 0
for line in data:
    target, nums = line.split(": ")
    target = int(target)
    nums = [int(n) for n in nums.split(" ")]
    res = recur_2(target, nums[0], nums[1:])
    if res:
        ans += target
print(ans)
