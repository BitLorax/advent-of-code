
import clipboard
import copy

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
        lines[i] = list(lines[i])

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]

res = 0
while True:
    changed = False
    n = copy.deepcopy(lines)
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == ".":
                continue
            elif lines[i][j] == "L":
                a = 0
                for k in range(8):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if ni >= 0 and ni < len(lines) and nj >= 0 and nj < len(lines[0]):
                        if lines[ni][nj] == "#":
                            a += 1
                if a == 0:
                    n[i][j] = "#"
                    changed = True
            else:
                a = 0
                for k in range(8):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if ni >= 0 and ni < len(lines) and nj >= 0 and nj < len(lines[0]):
                        if lines[ni][nj] == "#":
                            a += 1
                if a >= 4:
                    n[i][j] = "L"
                    changed = True
    lines = n
    if not changed:
        break

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == "#":
            res += 1

print(res)
clipboard.copy(res)
