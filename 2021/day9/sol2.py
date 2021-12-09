
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

dest = [[] for i in range(len(lines))]
for i in range(len(lines)):
    for j in range(len(lines[i])):
        dest[i].append(set())

def hash(x, y):
    return len(lines[0]) * y + x

def dfs(sx, sy, x, y):
    if x < 0 or x >= len(lines[0]) or y < 0 or y >= len(lines):
        return
    v = True
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or nx >= len(lines[0]) or ny < 0 or ny >= len(lines):
            continue
        if ti(lines[y][x]) > ti(lines[ny][nx]):
            dfs(sx, sy, nx, ny)
            v = False
    if v:
        dest[sy][sx].add(hash(x, y))
        if sx == 3 and sy == 0:
            print(str(sx) + " " + str(sy) + " " + str(x) + " " + str(y))

for y in range(len(lines)):
    for x in range(len(lines[0])):
        if ti(lines[y][x]) == 9:
            continue
        dfs(x, y, x, y)

res = 0
resl = []
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
            s = 0
            for ii in range(len(lines)):
                for jj in range(len(lines[0])):
                    # if ii == 0 and jj == 2:
                    #     print(dest[ii][jj])
                    #     print(len(dest[ii][jj]))
                    if len(dest[ii][jj]) > 1 or len(dest[ii][jj]) == 0:
                        continue
                    ddd = dest[ii][jj].pop()
                    if hash(j, i) == ddd:
                        if i == 2 and j == 2:
                            print(str(ii) + " " + str(jj))
                        s += 1
                    dest[ii][jj].add(ddd)
            resl.append(s)

print(resl)
resl = sorted(resl)
res = resl[-1] * resl[-2] * resl[-3]

print(res)
clipboard.copy(res)
