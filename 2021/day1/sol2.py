
res = 0
prev = -1
with open("input.txt", "r") as f:
    lines = f.readlines()
    for i in range(len(lines) - 2):
        s = 0
        for j in range(3):
            s += (int)(lines[i + j])
        if s > prev:
            res += 1
        prev = s
print(res - 1)

