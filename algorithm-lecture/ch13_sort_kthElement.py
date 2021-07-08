# ch13-lab3: k번째 수 구하기
import random
import time

def partition(v, a, b):
    i, j, pivot = a, b-1, v[b]
    while i <= j:
        if v[i] <= pivot: i += 1
        else:
            v[i], v[j] = v[j], v[i]
            j -= 1
    v[b], v[i] = v[i], pivot
    return i

def _kthElement(v, a, b, k):
    if a == b: return v[a] # 탈출 조건 
    c = partition(v, a, b )
    if c == k: return v[k]
    if k < c: return _kthElement(v, a, c-1, k)
    return _kthElement(v, c+1, b, k)

def kthElement(v, k):
    return _kthElement(v, 0, len(v)-1, k)



n = random.randrange(5000000, 10000000)
k = random.randrange(n)
print(n, k)

v = [ random.randrange(1000000) for _ in range(n)] 
ts = time.time()
r = kthElement(v, k)
et = int((time.time() - ts)*1000) #msec
print(r)
print(f"Elapsed time: {et}ms")


ts = time.time()
v.sort()
et = int((time.time() - ts)*1000) #msec
print(v[k])
print(f"Elapsed time: {et}ms")
