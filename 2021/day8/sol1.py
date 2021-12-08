
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
        lines[i] = lines[i].strip().split(" | ")[1].split()
        if len(lines[i]) == 1:
            lines[i] = lines[i][0]

res = 0
for line in lines:
    for i in line:
        if len(i) == 2 or len(i) == 4 or len(i) == 3 or len(i) == 7:
            res += 1

print(res)
clipboard.copy(res)
