from collections import deque
import sys
input = sys.stdin.readline

# G = 스타트링크, S = 현재 위치, U = 위로, D = 아래, F = 가장 높은 층
# 1층 부터 시작
f, s, g, u, d = map(int,input().split())
visitied = [-1] * (f + 1)

def bfs(start):
    q = deque()
    q.append(start)
    visitied[start] = 0

    while q:
        cur = q.popleft()

        if cur == g:
            return visitied[cur]
        
        for next in (cur + u, cur - d):
            if 0 < next <= f and visitied[next] == -1:
                visitied[next] = visitied[cur] + 1
                q.append(next)
    
    if visitied[g] == -1:
        return "use the stairs"

print(bfs(s))