with open("input.txt", "r") as f:
    data = f.read().split("\n")

list1 = []
list2 = []
for x in data:
    num1, num2 = [int(n) for n in x.split("   ")]
    list1.append(num1)
    list2.append(num2)

list1.sort()
list2.sort()

ans = 0

for i, n in enumerate(list1):
    ans += abs(n - list2[i])

print(ans)


# ------------------------------- #

with open("input.txt", "r") as f:
    data = f.read().split("\n")

list1 = []
dict2 = {}
for x in data:
    num1, num2 = [int(n) for n in x.split("   ")]
    list1.append(num1)
    dict2[num2] = dict2.get(num2, 0) + 1

ans = 0

for n in list1:
    ans += n * dict2.get(n, 0)

print(ans)
