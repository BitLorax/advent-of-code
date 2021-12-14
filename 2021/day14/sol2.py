
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

cdx = [1, -1, 0, 0]
cdy = [0, 0, 1, -1]
dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]
res = 0

m = {}
ms = {}
for line in lines[2:]:
    m[line[0]] = line[2]
    ms[line[0]] = 0

s = lines[0]
for i in range(len(s) - 1):
    ms[s[i:i + 2]] += 1

for t in range(40):
    nms = {}
    for k in ms:
        nms[k] = ms[k]
    for k in ms:
        a = m[k]
        b = k[0] + a
        c = a + k[1]
        nms[b] += ms[k]
        nms[c] += ms[k]
        nms[k] -= ms[k]
    ms = nms

mmm = {}
for k in ms:
    a = k[0]
    b = k[1]
    if a in mmm:
        mmm[a] += ms[k]
    else:
        mmm[a] = ms[k]
    if b in mmm:
        mmm[b] += ms[k]
    else:
        mmm[b] = ms[k]

mmm[s[0]] += 1
mmm[s[-1]] += 1

l = []
for k in mmm:
    l.append(ti(mmm[k] / 2))
l = sorted(l)
res = l[-1] - l[0]

print(res)
clipboard.copy(res)
