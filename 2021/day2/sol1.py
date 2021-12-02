
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
    for a, b in lines:
        if a == 'forward':
            x += ti(b)
        if a == 'up':
            y -= ti(b)
        if a == 'down':
            y += ti(b)
    res = x * y
print(res)

