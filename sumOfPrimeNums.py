# 1~100까지 소수의 합
# 소수: 1과 자기자신으로 밖에 나누어지지 않는 1이외의 정수

def isPrime(num):
    if num == 2: return True # 2 is prime numver
    if num < 2: return False
    if num%2 == 0: return False 
    
    # 소수(홀수) - 3~num까지의 홀수로 나누었을 때 나머지==0이라면 소수 x
    for i in range(3, num, 2) :
        if num%i == 0: return False

    return True

sum = 0
for i in range(1, 101):
    if isPrime(i): sum += i
print(sum)


"""
[OUTPUT]
1060
"""