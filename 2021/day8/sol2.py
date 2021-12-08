
import clipboard
import itertools

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
        lines[i] = lines[i].strip().split(" | ")
        lines[i][0] = lines[i][0].split()
        lines[i][1] = lines[i][1].split()

m = {"1110111": 0,
     "0010010": 1,
     "1011101": 2,
     "1011011": 3,
     "0111010": 4,
     "1101011": 5,
     "1101111": 6,
     "1010010": 7,
     "1111111": 8,
     "1111011": 9
}

res = 0
for line in lines:
    perms = list(itertools.permutations(list("abcdefg")))
    for perm in perms:
        pos = {}
        for i in range(len(perm)):
            pos[perm[i]] = i
        valid = True
        for i in line[0]:
            s = [0 for l in range(7)]
            for j in i:
                s[pos[j]] = 1
            ss = ""
            for k in s:
                ss += str(k)
            if ss not in m:
                valid = False
                break
        if valid:
            num = ""
            for i in line[1]:
                s = [0 for i in range(7)]
                for j in i:
                    s[pos[j]] = 1
                ss = ""
                for k in s:
                    ss += str(k)
                num += str(m[ss])
            res += ti(num)

print(res)
clipboard.copy(res)
