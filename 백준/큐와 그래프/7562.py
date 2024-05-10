import sys 
from collections import deque

input = sys.stdin.readline

t = int(input())

#나이트가 움직일 수 있는 경로
m = [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]]

def bfs(g, sx, sy, ex, ey, a):
    queue = deque()
    queue.append((sx,sy))

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + m[i][0]
            ny = y + m[i][1]

            if 0 <= nx < a and 0 <= ny < a and g[nx][ny] == 0:
                queue.append((nx,ny))
                g[nx][ny] = g[x][y] + 1

for i in range(t):
    a = int(input()) #체스크기
    sx, sy = map(int,input().split()) #시작 위치
    ex, ey = map(int,input().split()) #끝나야하는 위치
    if (sx == ex and sy == ey):
        print(0)
        continue
    g = [[0 for _ in range(a)] for _ in range(a)]
    bfs(g, sx, sy, ex, ey, a)
    print(g[ex][ey])