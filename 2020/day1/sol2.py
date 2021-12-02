
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

lines = tii(lines)

res = 0
for i in range(len(lines)):
    for j in range(i, len(lines)):
        for k in range(j, len(lines)):
            if lines[i] + lines[j] + lines[k] == 2020:
                res = lines[i] * lines[j] * lines[k]
                break

print(res)
clipboard.copy(res)
