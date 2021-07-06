# ch05-lab2: 성적등급 구하기
score = int(input('성적: '))

if score>=90: grade='A'
elif score>=80: grade='B'
elif score>=70: grade='C'
elif score>=60: grade='D'
else: grade='F'

print(f"성적: {score}, 등급: {grade}")