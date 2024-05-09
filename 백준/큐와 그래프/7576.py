import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int,input().split())

g = [list(map(int,input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


queue = deque()
for i in range(n):
    for j in range(m):
        if g[i][j] == 1:
            queue.append((i,j))
            

def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 0:
                queue.append((nx,ny))
                g[nx][ny] = g[x][y] + 1

bfs()
result = 0

for i in g:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result,max(i))

print(result-1)