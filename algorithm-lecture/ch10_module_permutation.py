# ch10-lab1: 재귀함수로 순열 구하기

# 재귀 함수로 순열 구하기
def perm(v, f, c, k, t):
    if c == k:
        print(t)
        return
    for i in range(len(v)):
        if f[i]: continue
        f[i] = True
        perm(v, f, c+1, k, t+(v[i], ))
        f[i] = False
        
v = input("리스트의 내용 입력 : ").split()
k = int(input("표시할 개수 입력 : "))

f = [False]*(len(v))

perm(v, f, 0, k, tuple())