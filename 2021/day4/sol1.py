
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

def bingo(board):
    for i in range(5):
        v = True
        for j in range(5):
            v = v and board[i][j] == "X"
        if v:
            return True
    for i in range(5):
        v = True
        for j in range(5):
            v = v and board[j][i] == "X"
        if v:
            return True
    v = True
    for i in range(5):
        v = v and board[i][i] == "X"
    if v:
        return True
    v = True
    for i in range(5):
        v = v and board[i][5 - 1 - i] == "X"
    if v:
        return True
    return False


res = 0
boards = []
i = 2
while i < n:
    boards.append(lines[i:i+5])
    i += 6

go = True
for i in lines[0].split(","):
    if not go:
        break
    for b in boards:
        for j in range(5):
            for k in range(5):
                if b[j][k] == i:
                    b[j][k] = "X"
    for b in boards:
        if bingo(b):
            won[kkk
            s = 0
            for j in range(5):
                for k in range(5):
                    if b[j][k] != "X":
                        s += ti(b[j][k])
            res = s * ti(i)
            go = False
            break


print(res)
clipboard.copy(res)
