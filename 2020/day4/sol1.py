
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

res = 0
m = {'byr': 0,
     'iyr': 0,
     'eyr': 0,
     'hgt': 0,
     'hcl': 0,
     'ecl': 0,
     'pid': 0,
     'cid': 0}
for i in range(len(lines)):
    if lines[i] == ['']:
        v = True
        for i in m:
            if i == 'cid':
                continue
            v = v and m[i] == 1
            m[i] = 0
        if v:
            res += 1
    else:
        for j in lines[i]:
            m[j[0:3]] = 1

print(res)
clipboard.copy(res)
