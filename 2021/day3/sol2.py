
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

v = [True for i in range(len(lines))]
c = len(lines)
for i in range(len(lines[0])):
    a = 0
    b = 0
    for j in range(len(lines)):
        line = lines[j]
        if not v[j]:
            continue
        if line[i] == '1':
            a += 1
        else:
            b += 1
    if a >= b:
        for j in range(len(lines)):
            if not v[j]:
                continue
            line = lines[j]
            if line[i] == '0':
                v[j] = False
                c -= 1
    else:
        for j in range(len(lines)):
            if not v[j]:
                continue
            line = lines[j]
            if line[i] == '1':
                v[j] = False
                c -= 1
    if c == 1:
        break
for i in range(len(v)):
    if v[i]:
        oxy = lines[i]

v2 = [True for i in range(len(lines))]
c = len(lines)
for i in range(len(lines[0])):
    a = 0
    b = 0
    for j in range(len(lines)):
        line = lines[j]
        if not v2[j]:
            continue
        if line[i] == '1':
            a += 1
        else:
            b += 1
    if a >= b:
        for j in range(len(lines)):
            if not v2[j]:
                continue
            line = lines[j]
            if line[i] == '1':
                c -= 1
                v2[j] = False
    else:
        for j in range(len(lines)):
            if not v2[j]:
                continue
            line = lines[j]
            if line[i] == '0':
                c -= 1
                v2[j] = False
    if c == 1:
        break
for i in range(len(v2)):
    if v2[i]:
        other = lines[i]

res = int(oxy, 2) * int(other, 2)

print(res)
clipboard.copy(res)
