# ch17-lab1: 입국심사

n = int(input())
io = list(map(int, input().split()))    # 입국심사관

# 심사관들이 최대 처리할 수 있는 입국자들의 수
def processCount(io, tm): # 입국심사관, 시간
    sum = 0
    for i in io:
        sum += tm // i
    return sum

# 심사관들 중에서 가장 처리시간이 짧은 심사관의 처리시간 
minio = min(io)

# left에는 해당 시간안에 절대 처리 못할 시간으로 설정
# right에는 해당 시간안데 항상 처리할 수 있는 시간으로 설정
left, right = minio-1, minio*n
while left < right-1:
    c = (left+right) // 2
    pc = processCount(io, c)
    if pc >=n: right = c
    else: left = c

print(right)



"""
[INPUT]
6
7 10

[OUTPUT]
28
"""