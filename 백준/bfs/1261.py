import sys
input = sys.stdin.readline
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m = map(int,input().split())
miro = [list(map(int, input().rstrip())) for _ in range(m)]
dist = [[-1] * n for _ in range(m)]

q = deque()
q.append((0,0))
dist[0][0] = 0

while q:
    x,y = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < m and 0 <= ny < n:
            if dist[nx][ny] == -1:
                if miro[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx,ny))
                else:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))

print(dist[m-1][n-1])