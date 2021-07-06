# ch05-lab3: 친구 리스트 확인
friends = input('친구들의 이름을 적으세요: ').split()
friend = input('이름을 입력하세요: ')

if friend in friends:
    print("{0}는 당신의 친구입니다".format(friend))
else:
    print("{0}는 당신의 친구가 아닙니다".format(friend))
