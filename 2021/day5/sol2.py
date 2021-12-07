
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
        lines[i] = lines[i].strip()
        if len(lines[i]) == 1:
            lines[i] = lines[i][0]

res = 0
l = []
for line in lines:
    line = line.split(" -> ")
    a = line[0].split(",")
    b = line[1].split(",")
    l.append([tii(a), tii(b)])

v = [[0 for y in range(1000)] for x in range(1000)]
for i in range(len(l)):
    p1 = l[i][0]
    p2 = l[i][1]
    if p1[0] == p2[0]:
        a = min(p1[1], p2[1])
        b = max(p1[1], p2[1])
        for j in range(a, b + 1):
            v[p1[0]][j] += 1
    elif p1[1] == p2[1]:
        a = min(p1[0], p2[0])
        b = max(p1[0], p2[0])
        for j in range(a, b + 1):
            v[j][p1[1]] += 1
    else:
        if p1[0] > p2[0]:
            p1, p2 = p2, p1
        for i in range(p2[0] - p1[0] + 1):
            if p2[1] > p1[1]:
                x = p1[0] + i
                y = p1[1] + i
                v[x][y] += 1
            else:
                x = p1[0] + i
                y = p1[1] - i
                v[x][y] += 1

for x in range(1000):
    for y in range(1000):
        if v[x][y] >= 2:
            res += 1

print(res)
clipboard.copy(res)
