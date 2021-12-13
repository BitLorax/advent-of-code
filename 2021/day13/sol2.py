
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

cdx = [1, -1, 0, 0]
cdy = [0, 0, 1, -1]
dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]
res = 0
pts = []
folds = []
for line in lines:
    if len(line) == 1:
        line = line[0].split(",")
        pts.append(tii(line))
    elif len(line) > 0 and line[0] == 'fold':
        line = line[2].split("=")
        folds.append([line[0], ti(line[1])])

for fold in folds:
    if fold[0] == 'y':
        for pt in pts:
            if pt[1] > fold[1]:
                pt[1] = fold[1] - (pt[1] - fold[1])
    else:
        for pt in pts:
            if pt[0] > fold[1]:
                pt[0] = fold[1] - (pt[0] - fold[1])
    pts = sorted(pts)
    new_pts = []
    for pt in pts:
        if len(new_pts) > 0 and new_pts[-1][0] == pt[0] and new_pts[-1][1] == pt[1]:
            continue
        new_pts.append(pt)
    pts = new_pts

xmax = 0
ymax = 0
for pt in pts:
    xmax = max(xmax, pt[0])
    ymax = max(ymax, pt[1])
xmax += 1
ymax += 1

a = [[0 for j in range(ymax)] for i in range(xmax)]
for pt in pts:
    a[pt[0]][pt[1]] = 1
for y in range(ymax):
    s = ""
    for x in range(xmax):
        if a[x][y] == 1:
            s += '#'
        else:
            s += '.'
    print(s)
