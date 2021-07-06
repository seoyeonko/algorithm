# ch04-lab3: 문자열 입력받고 콤마로 분리해 표시하기
s = input('친구들의 이름을 적어주세요: ').split()

print(s)
print(*s) # print(s[0], s[1], s[2], ..)
print('당신의 친구들은 %s입니다'%(", ".join(s)))