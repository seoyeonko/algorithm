# ch08-lab4: 요세푸스 문제 풀기

n, k = map(int, input().split())

queue = list(range(1, n+1))
# print(queue)

while len(queue) > 0:
    for _ in range(k-1): queue.append(queue.pop(0))
        # s = queue.pop(0)
        # queue.append(s)
    print(queue.pop(0))
    # s = queue.pop(0)
    # print(s)