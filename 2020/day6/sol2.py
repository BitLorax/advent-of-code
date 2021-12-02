
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
m = {}
for i in 'abcdefghijklmnopqrstuvwxyz':
    m[i] = 0
nn = 0
for line in lines:
    if line == '':
        for i in m:
            if m[i] == nn:
                res += 1
            m[i] = 0
        nn = 0
    else:
        for i in line:
            m[i] += 1
        nn += 1
for i in m:
    if m[i] == nn:
        res += 1
    m[i] = 0


print(res)
clipboard.copy(res)
