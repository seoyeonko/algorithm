# ch07-lab3: 팰린드롬 개수 구하기 
# 주어진 문자열에서 팰린드롬이 되는 부분수열의 개수 출력

# 팰린드롬 검사하는 함수
def isPalindrome(x):
    return x[::-1] == x

x = input()

# 중복되지 않는 부분수열 개수 - set 
sub = set()
for s in range(len(x)):
    for t in range(s+1, len(x)+1):
        sub.add(x[s:t])


count = 0
for s in sub:
    if isPalindrome(s): 
        print(s)
        count += 1

print(count)