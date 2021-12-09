
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

def amax(a):
    ret = a[0]
    for i in a:
        ret = max(ret, i)
    return ret

def amin(a):
    ret = a[0]
    for i in a:
        ret = min(ret, i)
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
lines = sorted(tii(lines))
lines = [0] + lines

mem = [-1 for i in range(len(lines) + 1)]
def solve(i):
    if i == len(lines) - 1:
        return 1
    if mem[i] != -1:
        return mem[i]

    ret = 0
    for j in range(1, 4):
        if i + j < len(lines) and lines[i + j] - lines[i] <= 3:
            ret += solve(i + j)
    mem[i] = ret
    return ret

res = solve(0)

print(res)
clipboard.copy(res)
