# ch13-lab1: 기본 정렬 구현 
# 선택, 삽입, 버블 정렬
import random
import time

def isSorted(v):
    for i in range(1, n):
        if v[i-1] > v[i]: return False
    return True


def selectionSort(v):
    n = len(v)
    for i in range(n-1): # 0 ~ n-2
        min = i # idx of min value
        for j in range(i+1, n): # i+1 ~ n-2
            if v[j] < v[min]: min = j
        v[i], v[min] = v[min], v[i] # swapping


def insertionSort(v):
    n = len(v)
    for i in range(1, n): # 1 ~ n-1
        t = v[i]
        last = i-1 
        while last >= 0 and v[last] > t: 
            v[last+1] = v[last]
            last -= 1
        v[last+1] = t 


def bubbleSort(v):
    n = len(v)
    for i in range(n-1): 
        isSwap = False
        for j in range(n-i-1): # 0 ~ n-i-2 # 버블(원소2개묶음)이 뒤에서 두번째 원소까지
            if v[j] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]
                isSwap = True
        if not isSwap: break
    


n = int(input("n= "))
v = [random.randrange(1, 1000000) for _ in range(n)] 
ts = time.time() # time stamp

# selectionSort(v)
# insertionSort(v)
bubbleSort(v)
et = int((time.time() - ts)*1000) # msec

print(v[:20])
print(f"Elapsed time is {et}ms.")

if isSorted(v): print("Sorted")
else: print("Not Sorted")

