# ch17-lab1: 하노이 탑

move = 0
res = 0

def hanoi(n, a, b, c):
    global move
    global res
    if n == 1:
        disk = a[1].pop()
        b[1].append(disk)
        move += 1
        if move == k: res = disk
        return
    hanoi(n-1, a, c, b)
    hanoi(1, a, b, c)
    hanoi(n-1, c, b, a)

k = int(input("Enter the number of moves : "))
st = [ 20-i for i in range(20) ]
hanoi(20, ("A", st), ("B", []), ("C", []))
print(res)

"""
for i in range(30):
    if k%2 == 1: 
        print(i+1)
        break
    k //= 2
"""

print(bin(k))
k = k & (-k)
print(bin(k))

for i in range(30):
    if (k & (i << 1)) != 0:
        print(i+1)
        break



"""
[INPUT]
Enter the number of moves : 5

[OUTPUT]
1
0b101
0b1

규칙 있음! bin(move)와 disk 변수의 상관관계 
"""