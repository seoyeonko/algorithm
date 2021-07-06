# ch07-lab2: 색종이의 넓이 구하기

# 널빤지에 색종이 붙이기
def post(palet, x, y):
    for i in range(y, y+10):
        for j in range(x, x+10):
            plate[i][j] = 1

# 널빤지 초기화            
plate = []
for i in range(100):
    plate.append([0]*100)


n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    post(plate, x, y)

# 널빤지에서 색종이가 붙읕 공간의 개수 구하기
count = 0
for i in range(100):
    for j in range(100):
        if plate[i][j] ==1: count += 1

print("넓이:", count)





"""
[INPUT]
10
1 3
8 7
13 2
7 6
21 21
19 15
1 20
21 0
3 19
8 17
"""