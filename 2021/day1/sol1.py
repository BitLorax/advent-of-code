
res = 0
prev = -1
with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        a = (int)(line)
        if a > prev:
            res += 1
        prev = a
print(res - 1)

