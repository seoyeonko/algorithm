# ch16-lab2: 최소 신장 트리 구하기 (Minimun Spanning Tree)
# Kruskal Algorithm

n, m = map(int, input().split())

# 배타적 집합 자료 생성
set = [ k for k in range(n) ]

# find set root
def getRoot(set, s):
	if s == set[s]: return s
	set[s] = getRoot(set, set[s])
	return set[s]

edges = [ ]
for _ in range(m):
	a, b, w = map(int, input().split())
	edges.append( (w, a-1, b-1) ) # w, a, b order for sorting
edges.sort()

mst = 0
for e in edges:
	(w, a, b) = e
	ra, rb = getRoot(set, a), getRoot(set, b)
	if ra == rb: continue		# if set a and set b is same
	set[rb] = ra				# union set a and set b
	mst += w
    # print("(%d <---> %d)"%(a+1, b+1))


print(mst)


"""
[INPUT]
3 3 
1 2 1
2 3 2
1 3 3

[OUTPUT]
3
"""