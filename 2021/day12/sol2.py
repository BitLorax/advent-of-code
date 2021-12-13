
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

conn = {}
for line in lines:
    line = line.split('-')
    if line[0] in conn:
        conn[line[0]].append(line[1])
    else:
        conn[line[0]] = [line[1]]
    if line[1] in conn:
        conn[line[1]].append(line[0])
    else:
        conn[line[1]] = [line[0]]

def dfs(cur, vis, v):
    global res
    if cur == 'end':
        res += 1
        return
    if cur in conn:
        for i in conn[cur]:
            if i == 'start':
                continue
            if i.isupper():
                dfs(i, vis, v)
            else:
                if i in vis:
                    if not v:
                        vis.append(i)
                        dfs(i, vis, True)
                        vis.remove(i)
                else:
                    vis.append(i)
                    dfs(i, vis, v)
                    vis.remove(i)

dfs('start', [], False)

print(res)
clipboard.copy(res)
