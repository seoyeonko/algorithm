# ch06-lab5: 약수의 개수 구하기
n= int(input('n = '))


# 1) 
divCount=0

for i in range(n):
    if (n % (i+1) == 0):
        divCount +=1
        # print(i+1, end=" ")
print("\n"+str(divCount)+"개")



# 2) root n algorithm
divCount = 0
k=1
while k*k < 0:
    if n%k == n: divCount += 1
    k += 1
if k*k == n: divCount+= 1
print(divCount)


