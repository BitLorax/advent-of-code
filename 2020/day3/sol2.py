
import clipboard

# Helper macros
def ti(s):
    return (int)(s)

def ts(i):
    return (str)(i)

def tii(ss):
    ret = []
    for i in ss:
        ret.append(ti(i))
    return ret

def tss(ii):
    ret = []
    for i in ii:
        ret.append(ts(i))
    return ret


# Read input
with open("input.txt", "r") as f:
    lines = f.readlines()
    n = len(lines)
    for i in range(n):
        lines[i] = lines[i].strip().split(" ")
        if len(lines[i]) == 1:
            lines[i] = lines[i][0]

res = 0
s = [0, 0, 0, 0, 0]
for i in range(len(lines)):
    n = len(lines[i])
    if lines[i][(1 * i) % n] == "#":
        s[0] += 1
    if lines[i][(3 * i) % n] == "#":
        s[1] += 1
    if lines[i][(5 * i) % n] == "#":
        s[2] += 1
    if lines[i][(7 * i) % n] == "#":
        s[3] += 1
    if i % 2 == 0 and lines[i][ti(i / 2) % n] == "#":
        s[4] += 1
res = s[0] * s[1] * s[2] * s[3] * s[4]

print(res)
clipboard.copy(res)
