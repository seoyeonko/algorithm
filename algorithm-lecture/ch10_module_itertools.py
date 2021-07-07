# ch10-lab2: Itertools로 구현

from itertools import permutations # import itertools 

v = input("리스트의 내용 입력 : ").split()
k = int(input("표시할 내용 개수 입력 : "))
    
for i in permutations(v,k): # itertools.permutations
    print(i)
    
