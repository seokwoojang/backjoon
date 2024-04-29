from collections import deque
import sys

n,m,v = map(int,input().split())

g = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
    g[a].sort()

visited = [False] * (n+1)

def dfs(g,v,visited):
    visited[v] = True
    print(v, end=' ')
    for i in g[v]:
        if not visited[i]:
            dfs(g,i,visited)

def bfs(g,start,visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end = ' ')

        for i in g[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(g,v,visited)
print()
visited = [False] * (n+1)
bfs(g,v,visited)