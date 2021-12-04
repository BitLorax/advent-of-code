
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
i = 0
while True:
    if visited[i]:
        res = acc
        break
    visited[i] = True
    a = lines[i][0]
    if a == 'nop':
        i += 1
    if a == 'acc':
        acc += ti(lines[i][1])
        i += 1
    if a == 'jmp':
        i += ti(lines[i][1])

print(res)
clipboard.copy(res)
