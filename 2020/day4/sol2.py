
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
            s = j[0:3]
            v = j[4:]
            if s == 'byr':
                if ti(v) >= 1920 and ti(v) <= 2002:
                    m[s] = 1
            if s == 'iyr':
                if ti(v) >= 2010 and ti(v) <= 2020:
                    m[s] = 1
            if s == 'eyr':
                if ti(v) >= 2020 and ti(v) <= 2030:
                    m[s] = 1
            if s == 'hgt':
                k = v[-2:]
                v = v[:-2]
                if k == 'cm':
                    if ti(v) >= 150 and ti(v) <= 193:
                        m[s] = 1
                if k == 'in':
                    if ti(v) >= 59 and ti(v) <= 76:
                        m[s] = 1
            if s == 'hcl':
                valid = v[0] == '#' and len(v) == 7
                for k in range(1, len(v)):
                    valid = valid and v[k] in (list)('0123456789abcdef')
                if valid:
                    m[s] = 1
            if s == 'ecl':
                if v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    m[s] = 1
            if s == 'pid':
                if len(v) == 9 and v.isnumeric():
                    m[s] = 1

print(res)
clipboard.copy(res)
