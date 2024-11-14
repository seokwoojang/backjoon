from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
ary = []
maxNum = 0

for i in range(n):
    ary.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        maxNum = max(ary[i][j], maxNum)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(sx, sy, value, visited):
    visited[sx][sy] = 1
    q = deque([(sx, sy)])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n:
                if ary[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

answer = 0
for i in range(maxNum):
    visited = [[0 for _ in range(n)] for r in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if ary[j][k] > i and visited[j][k] == 0:
                bfs(j,k,i,visited)
                cnt += 1
    
    answer = max(answer, cnt)

print(answer)