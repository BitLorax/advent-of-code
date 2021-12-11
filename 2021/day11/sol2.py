
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
a = []
for line in lines:
    r = []
    for i in line:
        r.append(ti(i))
    a.append(r)

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]

t = 0
while True:
    t += 1
    c = 0
    for x in range(10):
        for y in range(10):
            a[x][y] += 1
    while True:
        done = True
        for x in range(10):
            for y in range(10):
                if a[x][y] > 9:
                    c += 1
                    for k in range(8):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx >= 0 and nx < 10 and ny >= 0 and ny < 10:
                            if a[nx][ny] != 0:
                                a[nx][ny] += 1
                            done = False
                    a[x][y] = 0
        if done:
            break
    if c == 100:
        res = t
        break


print(res)
clipboard.copy(res)
