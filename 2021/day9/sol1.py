
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
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(len(lines)):
    for j in range(len(lines[0])):
        c = 0
        d = 0
        for k in range(4):
            ni = i + dy[k]
            nj = j + dx[k]
            if ni >= 0 and ni < len(lines) and nj >= 0 and nj < len(lines[0]):
                d += 1
                if ti(lines[ni][nj]) > ti(lines[i][j]):
                    c += 1
        if c == d:
            res += 1 + ti(lines[i][j])


print(res)
clipboard.copy(res)
