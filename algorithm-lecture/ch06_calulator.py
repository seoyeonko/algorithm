# ch06-lab4: 명령어를 통한 계산기
# 1)
while True:
    cmd = input().split()
    
    if cmd[0] == "quit": break # 먼저 보장하여 인덱스 에러 발생하지 않음 

    a = int(cmd[1])
    b = int(cmd[2])

    if cmd[0] == "add":
        print(a+b)
    elif cmd[0] == "sub":
        print(a-b)
    elif cmd[0] == "mul":
        print(a*b)
    elif cmd[0] == "div":
        if (b==0):
            print("0으로는 나눌 수 없음")
        print(a/b)
    else:
        print("정의되지 않은 명령어")


# 2) 더 깔끔한 풀이 
while True:
    cmd = input().split()

    if cmd[0] == "quit": break
    
    a = int(cmd[1])
    b = int(cmd[2])
    if cmd[0] == "add": print(a+b)
    elif cmd[0] == "sub": print(a-b)
    elif cmd[0] == "mul": print(a*b)
    elif cmd[0] == "div" and b != 0: print(a/b)

    
