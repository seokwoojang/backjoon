import sys
input = sys.stdin.readline
from collections import deque


def bfs(start):
    queue = deque()
    if start == 0:
        queue.append(1)
    else:
        queue.append(start)

    while queue:
        x = queue.popleft()

        if x == k:
            return dist[x]

        for nx in (x-1, x+1, x * 2):
            if 0<= nx <= 100000 and not dist[nx]:
                if nx == x * 2:
                    dist[nx] = dist[x]
                    queue.appendleft(nx)
                else:
                    dist[nx] = dist[x] + 1
                    queue.append(nx)
                
        

n, k = map(int,input().split())
dist = [0] * (100001)

if n == 0:
    if k == 0:
        print(0)
    else:
        print(bfs(n) + 1)
else:
    print(bfs(n))