
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
l = []
for line in lines:
    row = 0
    col = 0
    for i in range(7):
        if line[i] == 'B':
            row += pow(2, 6 - i)
    for i in range(7, 10):
        if line[i] == 'R':
            col += pow(2, 2 - (i - 7))
    l.append(row * 8 + col)
l = sorted(l)
for i in range(1, len(l)):
    if l[i] - l[i - 1] == 2:
        res = l[i] - 1

print(res)
clipboard.copy(res)
