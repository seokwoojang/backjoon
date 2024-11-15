from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

nx = [1, -1, 0, 0]
ny = [0, 0, 1, -1]

g = []
for i in range(n):
    g.append(list(map(int,input().split())))

def bfs(i, j, visited):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]

            if 0 <= dx < n and 0 <= dy < m and visited[dx][dy] == 0 and g[dx][dy] > 0:
                visited[dx][dy] = 1
                q.append((dx, dy))
def melt():
    melted = []

    for i in range(n):
        for j in range(m):
            if g[i][j] > 0:
                cnt = 0
                for k in range(4):
                    dx = i + nx[k]
                    dy = j + ny[k]
                    if 0 <= dx < n and 0 <= dy < m and g[dx][dy] <= 0:
                        cnt += 1
                if cnt > 0:
                    melted.append((i,j,cnt))
    
    for x, y, cnt in melted:
        g[x][y] = max(g[x][y]-cnt, 0)

year = 0
while True:
    melt()
    visited = [[0] * m for _ in range(n)]
    gcnt = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and g[i][j] > 0:
                bfs(i, j, visited)
                gcnt += 1
                if gcnt > 1:
                    print(year + 1)
                    exit(0)
    
    if gcnt == 0:
        print(0)
        break
    
    year +=1 

