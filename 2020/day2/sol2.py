
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
for line in lines:
    m = line[0]
    m = m.split("-")
    a = ti(m[0]) - 1
    b = ti(m[1]) - 1
    c = line[1][0]
    v = 0
    if a < len(line[2]) and line[2][a] == c:
        v += 1
    if b < len(line[2]) and line[2][b] == c:
        v += 1
    if v == 1:
        res += 1

print(res)
clipboard.copy(res)
