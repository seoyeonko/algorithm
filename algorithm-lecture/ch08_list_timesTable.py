# ch08-lab1: 리스트 내포를 이용한 구구단 리스트
# 2단부터 9단까지 


gugu = ["%s*%s=%s"%(i, j, i*j) for i in range(2, 10) 
                                for j in range(1, 10)] # %타입 형식 지정

gugu = ["{0}*{1}={2}".format(i, j, i*j) for i in range(2, 10) 
                            for j in range(1, 10)] # str format

gugu = [f"{i}*{j}={i*j}" for i in range(2, 10) 
                            for j in range(1, 10)] # f format


for g in gugu:
    print(g)

