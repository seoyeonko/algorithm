# ch16-lab3: 최단 경로 구하기


from heapq import *

Infity = 1000000000
n, m, s = map(int, input().split())
adj = [ [] for _ in range(n)]

for _ in range(m):                  # m개의 간선을 받음
    a, b, w = map(int, input().split())
    # 단방향 경로 t
    adj[a-1].append( (b-1, w) )     # a --> b with w

d = [ Infity ]*n    # Vertex values to Infity
visit = [ False ]*n # True if the vertex is visited
d[s-1] = 0            # Set vertex value to 0 at starting point 
pq = [ (0, s-1) ]     # priority queue ( d(weight), vertex index )

mst = 0
while len(pq) > 0:
    (_, u)  = heappop(pq)
    if visit[u]: continue
    visit[u] = True # mark this vertex u is visited
    
    # u: start vertex / v: end vertex
    for v, w in adj[u]:
        if visit[v] or d[v] <= w + d[u]: continue
        d[v] = w + d[u]
        heappush (pq, (w, v))

for dist in d:
    if dist == Infity: print("INF")
    else: print(dist)





"""
[INPUT]
5 6 1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

[OUTPUT]
0
2
3
7
INF
"""
