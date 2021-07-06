# ch06-lab1: 문자열 거꾸로 출력하기
s = input('문자열: ')

# 1) 가장 간단한 방법 
print(s[::-1]) 

# 3) 사용 빈도가 높음
for i in range(len(s)-1, -1, -1):
    print(s[i], end="")
print("")


# 2) 문자열 연산을 통한 방법 - 효율 떨어짐
rev=""
for c in s:
    rev = c + rev
print(rev)