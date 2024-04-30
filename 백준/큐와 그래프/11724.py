from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int,input().split())

g = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

visited = [False] * (n+1)

# def dfs(v):
#     visited[v] = True
#     for i in g[v]:
#         if not visited[i]:
#             dfs(i)

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in g[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

count = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        count+=1
print(count)