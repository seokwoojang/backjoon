import sys
input = sys.stdin.readline
from collections import deque

count = 0

def path(x):
    arr=[]
    temp = x
    for _ in range(dist[x] + 1):
        arr.append(temp)
        temp = move[temp]
    print(' '.join(map(str, arr[::-1])))

def bfs(start):
    global count

    queue = deque()
    queue.append(start)

    while queue:
        x = queue.popleft()

        if x == k:
            print(dist[x])
            path(x)
            return

        for nx in (x-1, x+1, x * 2):
            if 0<= nx <=100000 and not dist[nx]:
                dist[nx] = dist[x] + 1
                queue.append(nx)
                move[nx] = x
        

n, k = map(int,input().split())
dist = [0] * (100001)
move = [0] * (100001)
bfs(n)