# ch06-lab2: 1부터 n까지의 합 
n = int(input("n: "))

# 1) while
sum = 0
i=1
while(i<=n):
    sum += i
    i += 1
print(sum)


# 2) for
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)
