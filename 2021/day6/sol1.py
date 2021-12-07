
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

res = 0
line = tii(lines[0].split(","))
m = {}
for i in line:
    if i in m:
        m[i] += 1
    else:
        m[i] = 1
for d in range(256):
    for i in m:
        line[i] -= 1
        if line[i] == -1:
            line[i] = 6
            line.append(line[i] + 2)

res = len(line)


print(res)
clipboard.copy(res)
