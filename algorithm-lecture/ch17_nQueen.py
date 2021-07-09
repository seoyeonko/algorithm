# ch17-lab2: N Queen
from itertools import permutations
import time

n = int(input("n= "))
v = [ k for k in range(n) ]

# 1) Permitation method -> n*n! 
def isValid(qs):
    d1, d2 = set(), set()
    for i in range(len(qs)):
        if qs[i]-i in d1: return False
        if qs[i]+i in d2: return False
        d1.add(qs[i]-i)
        d2.add(qs[i]+i)
        return True

ts = time.time()
cases = 0
for k in permutations(v):
	if isValid(k):
		cases += 1
et = int((time.time() - ts)*1000)

print(cases)
print(f"Elapsed time is {et}ms.")



# 2) Backtracking algorithm 
def backtrack(c, n, qs, d1, d2): # col, num of col, queen set, d1, d2
    if c == n: return 1
    count = 0
    for i in range(n):
        if i in qs: continue
        if i+c in d1: continue
        if i-c in d2: continue
        qs.add(i)
        d1.add(i+c)
        d2.add(i-c)
        count += backtrack(c+1, n, qs, d1, d2)
        qs.remove(i)
        d1.remove(i+c)
        d2.remove(i-c)
    return count
ts = time.time()
print(backtrack(0, n, set(), set(), set()))
et = int((time.time() - ts)*1000)
print(f"Elapsed time is {et}ms.")


"""
[INPUT]
n = 4


[OUTPUT]
(1, 3, 0, 2)
(2, 0, 3, 1)
2
"""
