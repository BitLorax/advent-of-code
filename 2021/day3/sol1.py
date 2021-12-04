
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
s = ""
e = ""
for i in range(len(lines[0])):
    a = 0
    b = 0
    for line in lines:
        if line[i] == '1':
            a += 1
        else:
            b += 1
    if a > b:
        s += '1'
        e += '0'
    else:
        s += '0'
        e += '1'

res = int(s, 2) * int(e, 2)

print(res)
clipboard.copy(res)
