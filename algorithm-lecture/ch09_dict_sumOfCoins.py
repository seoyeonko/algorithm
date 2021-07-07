# ch09-lab2: 동전 합의 경우의 수
# Hint : 재귀함수와 딕셔너리를 사용

def comb(h, c, coins, amount):
    if c == len(coins):
        if amount in h: h[amount] += 1
        else: h[amount] = 1
        return
    comb(h, c+1, coins, amount)
    comb(h, c+1, coins, amount+coins[c])

# 입력으로부터 코인들을 가져옵니다
coins = list(map(int, input().split()))

# 빈도를 저장하기 위해 딕셔너리 생성
hist = { }
# 재귀함수를 통하여 빈도수 저장
comb(hist, 0, coins, 0)
# 동전을 하나도 사용하지 않은 경우 삭제
del(hist[0])

# 경우의 수가 최대이면서, 가장 적은 금액 선정
maxv, maxi = 0, 0
for k in hist:
    if hist[k] > maxv:
        maxv, maxi = hist[k], k
    elif hist[k] == maxv and k < maxi:
        maxi = k

print(maxi)

 