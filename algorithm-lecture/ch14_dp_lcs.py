#  ch14-lab2: 가장 긴 공통 부분 수열(LCS) 구하기

a, b = input().split()
na, nb = len(a), len(b)
dp = [ [0]*(nb+1) for _ in range(na+1) ] # 리스트 내포로 생성 


# 1) 재귀함수 미사용
for i in range(1, na+1):
    for j in range(1, nb+1):
        if a[i-1] == b[j-1]:
             dp[i][j] = dp[i-1][j-1]+1
        else: 
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
print(dp[na][nb])


# 2) 재귀함수 사용
def lcs(a, b, x, y):
    if x == 0 or y == 0: return 0 # 탈출 조건 
    if dp[x][y] != None: return dp[x][y]
    if a[x-1] == b[y-1]:
        dp[x][y] = lcs(a, b, x-1, y-1)+1
        return dp[x][y]
    dp[x][y] = max(lcs(a, b, x-1, y), lcs(a, b, x, y-1))
    return dp[x][y]

dp = [[None]*(nb+1) for _ in range(na+1)]
print(lcs(a, b, len(a), len(b)))