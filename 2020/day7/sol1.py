
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
go_in = {}
for line in lines:
    a = " ".join(line[0].split(" ")[:-1])
    b = line[1][:-1].split(", ")
    for bag in b:
        bag = " ".join(bag.split(" ")[1:-1])
        if bag in go_in:
            go_in[bag].append(a)
        else:
            go_in[bag] = [a]

s = set()
def recurse(bag):
    if bag in s:
        return
    s.add(bag)
    if bag in go_in:
        for i in go_in[bag]:
            recurse(i)
recurse("shiny gold")
res = len(s) - 1

print(res)
clipboard.copy(res)
