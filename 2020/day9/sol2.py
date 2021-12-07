
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
targ = 0
lines = tii(lines)
for i in range(25, len(lines)):
    v = False
    for j in range(i - 25, i):
        for k in range(j, i):
            if lines[j] + lines[k] == lines[i]:
                v = True
    if not v:
        targ = lines[i]
        break

hi = 0
s = 0
for lo in range(len(lines)):
    while hi < len(lines) and s < targ:
        s += lines[hi]
        hi += 1
    if s == targ and hi - lo >= 2:
        nmin = lines[lo]
        nmax = lines[lo]
        for i in range(lo, hi):
            nmin = min(nmin, lines[i])
            nmax = max(nmax, lines[i])
        res = nmin + nmax
        break
    s -= lines[lo]


print(res)
clipboard.copy(res)
