# ch09-lab1: 문자열로 원하는 값 찾기

d = {} # create dictionary

while True:
    cmd = input().split()

    if cmd[0] == "Q": break
    if cmd[0] == "A":
        d[cmd[1]] = int(cmd[2])
    elif cmd[0] == "F":
        if cmd[1] in d: # exits cmd in dictionry?
            print(d[cmd[1]])
        else:
            print("Not Found")


