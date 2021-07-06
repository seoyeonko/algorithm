# ch07-lab1: 배수의 합 계산
# 1) 
def sum(n, m):
    s = 0
    for i in range(m, n+1, m): # m부터 n+1까지 m씩 증가
        s += i
    return s
    
# 2) % 연산 이용 
def sum1(n, m):
    s = 0
    for i in range(1, n+1):
        if i%m == 0 : s += i
    return s

# 3) 재귀함수 이용 - 효율 굉장히 비효율적
def sum2(n, m):
    if n == 0: return 0 # 탈출 조건
    
    if n%m ==0: return n+sum2(n-1, m)
    return sum2(n-1, m)

# 4) 반복함수 이용 
def mulRange(n, m):
    for i in range(m, n+1, m):
        yield i

def sum3(n, m):
    s = 0
    for i in mulRange(n, m):
        s += i
    return s


n, m = map(int, input().split())
print(sum(n, m))
print(sum1(n, m))
print(sum2(n, m))
print(sum3(n, m))


