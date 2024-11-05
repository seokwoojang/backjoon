import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for i in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)
ans = -1
def dfs(v, cnt):
    global ans

    if v == b:
        ans = cnt

    visited[v] = True

    for g in graph[v]:
        if not visited[g]:
            dfs(g, cnt + 1)

dfs(a, 0)
print(ans)