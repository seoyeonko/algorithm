# ch16-lab2: 최소 신장 트리 구하기 (Minimun Spanning Tree)
# Prim Algorithm
# heapq: priority queue

from heapq import *

Infity = 1000000000
n, m = map(int, input().split())
adj = [ [] for _ in range(n)]

for _ in range(m):                  # m개의 간선을 받음
    a, b, w = map(int, input().split())
    # 간선 2개 (무향 graph)
    adj[a-1].append( (b-1, w) )     # a --> b with w
    adj[b-1].append( (a-1, w) )     # b --> a with w

d = [ Infity ]*n    # Vertex values to Infity
visit = [ False ]*n # True if the vertex is visited
d[0] = 0            # Choice a vertex randomly 
pq = [ (0, 0) ]     # priority queue ( d(weight), vertex index )

mst = 0
while len(pq) > 0:
    (_, u)  = heappop(pq)
    if visit[u]: continue
    visit[u] = True # mark this vertex u is visited
    mst += d[u]
    
    # u: start vertex / v: end vertex
    for v, w in adj[u]:
        if visit[v] or d[v] <= w: continue
        d[v] = w
        heappush (pq, (w, v))

print(mst)
print(d)


"""
[INPUT]
5 8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3

[OUTPUT]
5
"""