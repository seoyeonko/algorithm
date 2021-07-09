# ch16-lab1: 섬의 개수 구하기 

def dfs(map, r, c, n, m):
    map[r][c] = 0 # 방문했다고 표시
    dxy = ( (0, 1), (1, 0), (0, -1), (-1, 0) )
    for d in dxy:
        nr, nc = r + d[0], c + d[1] # new row, column
        # 경계선 검사 
        if nr < 0 or nr >= n: continue # 볼 필요 없음
        if nc < 0 or nc >= m: continue
        if map[nr][nc] == 0: continue
        dfs(map, nr, nc, n, m)


n, m = map(int, input().split()) # n: 줄의 개수, m: 한 문자열의 개수 

# 2차원 배열
map = [ [0]*m for _ in range(n) ] # n*m 배열 / reference 문제를 위해 내포 사용함

for i in range(n):
    s = input()
    for j in range(m):
        if s[j] == "1": map[i][j] = 1 

count = 0
for i in range(n):
    for j in range(m):
        if map[i][j] == 1: # 땅이 존재함
            count += 1
            dfs(map, i, j, n, m)


print(count)



"""
[INPUT]
6 8
01110000
01100110
01111011
00000011
01110110
01111110

[OUPUT]
2
"""