# ch05-lab1: 절대값 구하기
x = int(input('x = '))

# 1) 수식으로만 구하기 - if 사용 x
print(x*((x>0)*2-1) )

# 2) if문으로 출력
if x>0:
    print(x)
else:
    print(-x)

if x>0: print(x)
else: print(-x)

# 3) 한 줄 if문
print(x if x>0 else -x)

# list 값 이용해 구현
ft = [1, -1]
print(x *ft[x<0])

# if-elif-else를 대체
mo = ["모두 거짓", "A만 참", "B만 참", "모두 참"]
print(mo[(x<=0 + (x>10)*2)])




