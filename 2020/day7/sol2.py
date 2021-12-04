
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
        lines[i] = lines[i].strip().split(" contain ")
        if len(lines[i]) == 1:
            lines[i] = lines[i][0]

res = 0
contains = {}
for line in lines:
    a = " ".join(line[0].split(" ")[:-1])
    b = line[1][:-1].split(", ")
    contains[a] = []
    for bag in b:
        bag = " ".join(bag.split(" ")[:-1])
        contains[a].append(bag)

def recurse(bag):
    ret = 1
    for i in contains[bag]:
        a = i.split(" ")
        if a[0] == 'no':
            continue
        ret += ti(a[0]) * recurse(" ".join(a[1:]))
    return ret
res = recurse("shiny gold") - 1

print(res)
clipboard.copy(res)
