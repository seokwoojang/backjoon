from collections import deque
import sys

n,m,v = map(int,input().split())

g = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

for i in g:
    i.sort()

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in g[v]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end = ' ')

        for i in g[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)