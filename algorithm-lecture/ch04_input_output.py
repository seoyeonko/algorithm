# t = input('이름과 나이: ').split()
# name, age = t[0], int(t[1])
# print(name, age)

# print('hi' 'name') # 공백 없이 출력
# print('hi', 'name') # 공백 존재
# print('hi', end="bye")


# ch04-lab1: 사용자 정보 출력
name = input('이름: ')
birth = input('생년월일: ')
byear = int(birth[:4])
age = 2021 - byear

print("-"*20)
print(f"  이름  | {name:^10}")
print(f"  나이  | {age:^10}")
print(f" 생년월일| {birth[:4]}년 {birth[4:6]}월 {birth[6:]}일")
print("-"*20)


