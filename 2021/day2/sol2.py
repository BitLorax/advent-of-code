
def ti(s):
    return (int)(s)

def ts(i):
    return (str)(i)


res = 0
with open("input.txt", "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip().split(" ")

    x = 0
    y = 0
    aim = 0
    for a, b in lines:
        if a == 'forward':
            x += ti(b)
            y += aim * ti(b)
        if a == 'up':
            aim -= ti(b)
        if a == 'down':
            aim += ti(b)
    res = x * y
res = x * y
print(res)

