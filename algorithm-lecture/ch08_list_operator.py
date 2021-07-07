# ch08-lab3: 후위 연산자 계산하기

expr = input().split()

# stack 생성 
stack = []

for v in expr:
    if v =="+" or v=="-" or v=="*" or v=="/":
        b = stack.pop()
        a = stack.pop()

        if v == "+": stack.append(a+b)
        elif v == "-": stack.append(a-b)
        elif v == "*": stack.append(a*b)
        else: stack.append(a/b)
    else: stack.append(float(v))

print(stack[0]) # 모든 연산을 마친 후, stack에는 하나의 값만 남아있음 

    