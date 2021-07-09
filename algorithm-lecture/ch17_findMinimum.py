# ch17-lab3: 여러 개의 구간에서 최소값 찾기

import random
random.seed(100)

n, m = map(int, input().split())

v = [ random.randrange(1000) for _ in range(n) ]
w = [ (random.randrange(n//2),  random.randrange(n//2, n)) for _ in range(m) ]

print(v, w)

for s in w:
    mm = v[s[0]] # mm 최소값
    for i in range(s[0]+1, s[1]+1):
        mm = min(mm, v[i])
    print(mm)

Infty = 1000000000

def initSeg(tree, r, v, a, b):
    if a == b:
        tree[r] == v[a]
        return tree[r]
    c = (a+b)//2
    tree[r] = min(initSeg(tree, r*2, v, a, c), initSeg(tree, r*2+1, v, c+1, b))
    return tree[r]


def getSeg(tree, r, a, b, f, t):
    if t < a or b < f: return Infty
    if f <= a and b <= t : return tree[r]
    c = (a+b)//2
    return min(getSeg(tree, r*2, a, c, f, t), getSeg(tree, r*2+1, c+1, b, f, t))


tree = [0]*(4*n)
initSeg(tree, 1, v, 0, n-1)

for s in w:
    print(getSeg(tree, 1, 0, n-1, s[0], s[1]))




"""
[INPUT]
10 5

[OUTPUT]
-

"""