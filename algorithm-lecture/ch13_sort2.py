# ch13-lab2: 고급 정렬 구현
# 합병, 퀵, 힙 정렬
import random
import time

temp = [0]*1000000

def isSorted(v):
    for i in range(1, n):
        if v[i-1] > v[i]: return False
    return True


def selectionSort(v, a, b):
    for i in range(a, b): # 0 ~ n-2
        min = i # idx of min value
        for j in range(i+1, b+1): # i+1 ~ n-2
            if v[j] < v[min]: min = j
        v[i], v[min] = v[min], v[i] # swapping


# 병합 정렬 - merge 함수 
def merge(v, a, c, b):
    global temp # 전역 변수 사용 
    i, j, k = a, c+1, 0
    while i <= c and j <= b:
        if v[i] <= v[j]:
            temp[k] = v[i]
            i += 1
        else:
            temp[k] = v[j]
            j += 1
        k += 1
    while i <= c:
        temp[k] = v[i]
        i, k = i+1, k+1
    while j <= b:
        temp[k] = v[j]
        j, k = j+1, k+1
    for i in range(k): 
        v[a+i] = temp[i]

# 병합 정렬
def mergeSort(v, a, b):
    if a == b: return # 재귀함수의 탈출조건
    c = (a+b)//2 # 중간값
    mergeSort(v, a, c)
    mergeSort(v, c+1, b)
    merge(v, a, c, b)


# 퀵 정렬 - partition 함수
def partition(v, a, b):
    pivot, i, j = v[b], a, b-1
    while i <= j:
        if v[i] <= pivot: i += 1
        else: 
            v[i], v[j] = v[j], v[i]
            j -= 1
    v[i], v[b] = pivot, v[i]
    return i

# 퀵 정렬
def quickSort(v, a, b):
    if a >= b: return # 재귀함수의 탈출조건 
    c = partition(v, a, b)
    quickSort(v, a, c-1)
    quickSort(v, c+1, b)


# 힙 정렬
# 재귀적 관점 없이 작성 (forward(비재귀) 프로그램 형식!)
def heapify(v, r, n): # r(root)
    while r*2+1 < n:
        large = r*2+1
        if large < n-1 and v[large] < v[large+1]: large += 1
        if v[r] >= v[large]: return
        v[r], v[large] = v[large], v[r]
        r = large

def buildheap(v, n):
    for r in range(n//2-1, -1, -1):
        heapify(v, r, n)

def heapSort(v):
    n = len(v)
    buildheap(v, n)
    for i in range(1, n):
        v[0], v[n-i] = v[n-i], v[0]
        heapify(v, 0, n-i)


n = int(input("n= "))
v = [random.randrange(1, 1000000) for _ in range(n)] 
ts = time.time() # time stamp

# selectionSort(v, 0, n-1)
# mergeSort(v, 0, n-1)
# quickSort(v, 0, n-1)
heapSort(v)
et = int((time.time() - ts)*1000) # msec

print(v[:20])
print(f"Elapsed time is {et}ms.")

if isSorted(v): print("Sorted")
else: print("Not Sorted")

