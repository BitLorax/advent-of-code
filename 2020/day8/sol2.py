
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
        lines[i] = lines[i].strip().split(" ")
        if len(lines[i]) == 1:
            lines[i] = lines[i][0]

res = 0
acc = 0
visited = [False for i in range(n)]
def recurse(i, acc, changed):
    global res
    if i == n:
        res = acc
        return
    if visited[i]:
        return
    visited[i] = True
    a = lines[i][0]
    if a == 'nop':
        recurse(i + 1, acc, changed)
        if not changed:
            recurse(i + ti(lines[i][1]), acc, True)
    if a == 'acc':
        recurse(i + 1, acc + ti(lines[i][1]), changed)
    if a == 'jmp':
        recurse(i + ti(lines[i][1]), acc, changed)
        if not changed:
            recurse(i + 1, acc, True)
    visited[i] = False
recurse(0, 0, False)

print(res)
clipboard.copy(res)
