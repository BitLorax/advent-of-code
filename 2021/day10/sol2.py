
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
        if len(lines[i]) == 1:
            lines[i] = lines[i][0]

res = 0
s = []
for line in lines:
    l = []
    v = True
    for j in range(len(line)):
        i = line[j]
        if i == '(':
            l.append(i)
        elif i == '[':
            l.append(i)
        elif i == '{':
            l.append(i)
        elif i == '<':
            l.append(i)
        elif i == ')':
            if l[-1] != '(':
                v = False
            else:
                l = l[:-1]
        elif i == ']':
            if l[-1] != '[':
                v = False
            else:
                l = l[:-1]
        elif i == '}':
            if l[-1] != '{':
                v = False
            else:
                l = l[:-1]
        elif i == '>':
            if l[-1] != '<':
                v = False
            else:
                l = l[:-1]
    if v:
        if len(l) > 0:
            ss = 0
            for j in range(len(l) - 1, -1, -1):
                i = l[j]
                ss *= 5
                if i == '(':
                    ss += 1
                elif i == '[':
                    ss += 2
                elif i == '{':
                    ss += 3
                elif i == '<':
                    ss += 4

            s.append(ss)

s = sorted(s)
res = s[ti(len(s) / 2)]

print(res)
clipboard.copy(res)
