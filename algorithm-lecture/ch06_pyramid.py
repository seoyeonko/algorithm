# ch06-lab3: 피라미드 그리기 - 직각 삼각형
n = int(input("n="))

# 1) 이중 for loop
for i in range(n):
    for _ in range(i+1):
        print("*", end="")
    print("") # 줄바꿈

# 2) 문자열 연산을 통한 방법 - 권장!!
for n in range(n):
    print("*"*(n+1))

# 3) 문자열 formating 이용 
stars = "*"*n # 곱 연산을 한번만 진행함! 
for i in range(1, n+1):
    print("%.*s"%(i, stars))



# ch06-lab4: 피라미드 그리기 - 이등변 삼각형
# 1)
for i in range(n):
    print("%s%s"%(" "*(n-i-1), "*"*(2*i+1)))
    # print(" "*(n-i-1) + "*"*(2*i+1))

# 2)
stars = "*"*(2*n-1)
for i in range(1, n+1):
    print("%*.*s"%(n+i-1, 2*i-1, stars))
    # print("%5.1s"%stars) # n=1 # 5.1s: ____*
    # print("%6.3s"%stars) # n=2 # 6.3s: ___***
    # print("%6.3s"%stars) # n=2 # 7.5s: __*****
    # 포맷팅으로 자리수만큼 비어있는 공간은 공백 처리


