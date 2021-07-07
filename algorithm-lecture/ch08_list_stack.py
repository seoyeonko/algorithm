# ch08-lab2: 스택 구현 및 테스트
# 스택을 구현하고 스택을 테스트하는 프로그램 작성 (push, pup, top, empty 기능 구현 )

# stack에 newItem을 넣는다.
def push(stack, newItem):
    stack.append(newItem)

# stack에서 최상위 아이템을 삭제하고 그 아이템을 반환
def pop(stack):
    return stack.pop()

# stack에서 최상위 아이템을 반환
def top(stack):
    return stack[-1]

# stack이 비어있으면 True 반환
def empty(stack):
    return len(stack) == 0

stack = []
while True:
    cmd = input().split()
    if cmd[0] == "quit": break
    if cmd[0] == "push":
        push(stack, int(cmd[1]))
    elif cmd[0] == "pop":
        print(pop(stack))
    elif cmd[0] == "top":
        print(top(stack))
    elif cmd[0] == "empty":
        print(empty(stack))