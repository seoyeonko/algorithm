s = "홍길동 성춘향 이몽룡"
print(s)

sl = s.split()
print(sl)
print(len(sl))

a = sl[:2]
print(a)

b = sl[-2:]
print(b)

c = sl[:]
d = sl
print(c)
print(d)

# id값은 각각 다름
print(id(sl))
print(id(a))
print(id(b))
print(id(c))
print(id(d))


# 참조
M = [12, [1,2,3], 15]
a = M[:2]
print(a)
print(id(M))
print(id(a))

M[1][0] = 5
print(M)
print(a) # 결과 주의!

#
M = [0]*10
print(M)
M = [[0]*5] *3
print(M)
M[0][0] = 5
print(M)
# 동일한 레퍼런스를 참조함
print(id(M[0]))
print(id(M[1]))

# ----------------
# 다양한 자료형 연산
a = [3, 2, 4]
a.append(7)
print(a)
a.insert(0, 1)
print(a)
a.insert(len(a), 10)
print(a)
a.pop()
print(a)
print(a.pop(0))
print(a)

# ----------------
# 비트 연산자 활용
print(bin(11))
print(bin(6))
print(int("1111", 2))
print(11 | 6)
print(int("101100", 2))
print(11 << 2)
# 2의 k승 곱 - 11 * 2^2 = 44
# Left shift: 원래 숫자 * 2^k를 곱함
# Right shift: 원래 숫자 * 2^(-k) 곱함 (2^k를 나눔)
# 비트 연산자: 곱하기/나누기보다 연산 속도가 훨씬 빠르다!!


