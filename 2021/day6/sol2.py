
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
        lines[i] = lines[i].strip().split()
        if len(lines[i]) == 1:
            lines[i] = lines[i][0]

res = 0
line = tii(lines[0].split(","))
m = [0 for i in range(9)]
for i in line:
    m[i] += 1

for d in range(256):
    a = m[0]
    for i in range(8):
        m[i] = m[i + 1]
    m[8] = 0
    m[6] += a
    m[8] += a

for i in m:
    res += i


print(res)
clipboard.copy(res)
