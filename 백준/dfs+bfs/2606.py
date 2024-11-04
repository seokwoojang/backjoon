import sys
input = sys.stdin.readline

n = int(input())
a = int(input())
ary = []
for i in range(a):
    ary.append(list(map(int,input().split())))
graph = [[] for _ in range(n + 1)]

for i in range(a):
    graph[ary[i][0]].append(ary[i][1])
    graph[ary[i][1]].append(ary[i][0])

visited = [False] * (n + 1)
def dfs(v):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(1)
cnt = -1
for i in visited:
    if i:
        cnt+= 1
print(cnt)