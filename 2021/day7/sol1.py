
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
        lines[i] = lines[i].strip().split()
        if len(lines[i]) == 1:
            lines[i] = lines[i][0]

res = -1
line = tii(lines[0].split(","))
for i in range(0, 1000):
    s = 0
    for j in line:
        s += abs(j - i)
    if res == -1:
        res = s
    else:
        res = min(res, s)


print(res)
clipboard.copy(res)
