
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
for line in lines[2:]:
    m[line[0]] = line[2]

s = lines[0]
for t in range(10):
    ns = ''
    for i in range(len(s) - 1):
        a = s[i:i + 2]
        ns += s[i]
        ns += m[a]
    ns += s[ - 1]
    s = ns

mm = {}
for i in s:
    if i in mm:
        mm[i] += 1
    else:
        mm[i] = 1
l = []
for k in mm:
    l.append(mm[k])
l = sorted(l)
res = l[-1] - l[0]

print(res)
clipboard.copy(res)
