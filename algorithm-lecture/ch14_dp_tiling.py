#  ch14-lab1: 2*n 타일링

# 점화식
# n = 1; 1
# n = 2; 3
# n = 3; 5
# n = 4; 11
# n = 5; 21
# n = 6; 43
# n = 7; 85
# n = 8; 171
# 1<= n <= 100

# t(0)=1
# t(1)=1
# t(n) = t(n-1) + 2t(n-2)


dp = [None]*2000
def tiling(n):
    if n == 0 or n == 1: return 1
    if dp[n] != None: return dp[n]
    dp[n] = tiling(n-1) + 2*tiling(n-2)
    return dp[n]

n = int(input("n : "))
print(tiling(n))
print((2**(n+1) + 1-2*(n%2))//3)