# ch10-lab3: 가장 긴 길의의 증가하는 부분 수열
# algorithm
# 1) 리스트에 있는 문자들을 차례대로
# 2) 해당 문자의 왼쪽에 있는 문자들 중에 작은 값에 대해서 저장된 값이 가장 큰 것을 선택
# 3) 현재 위치에 그 값 +1 하여 저장
# 4) 저장된 값 중 최대값 출력

# 1 3 5 4 5 7 
"""
append()
"""
# v = list(map(int, input().split()))
# d = []

# for i in range(len(v)):
#     maxv = 0
#     for j in range(i): # 0 ~ i-1
#         if v[j] < v[i] and d[j] > maxv: maxv = d[j]
#     d.append(maxv + 1)

# maxv = 0
# for i in range(len(v)):
#     if d[i] > maxv: maxv = d[i]

# print(maxv)


"""
bisect module
"""
from bisect import bisect_left
import random

#v = list(map(int, input().split()))
v = [ random.randrange(1, 1000000) for _ in range(20000) ]
d = []

for i in range(len(v)):
    maxv = 0
    for j in range(i):
        if v[j] < v[i] and d[j] > maxv: maxv = d[j]
    d.append(maxv+1)

maxv = 0
for i in range(len(v)):
    if d[i] > maxv: maxv = d[i]

print(maxv)

#---------------------------------------------
d = [ v[0] ]
for i in range(1, len(v)):
    if v[i] > d[-1]:
        d.append(v[i])
    else:
        idx = bisect_left(d, v[i])
        d[idx] = v[i]
print(len(d))