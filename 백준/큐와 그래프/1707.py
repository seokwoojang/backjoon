import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

k = int(input())

def dfs(start, visited, g, group):
    visited[start] = group

    for v in g[start]:
        if visited[v] == 0:
            result = dfs(v, visited,g,-group)
            if not result:
                return False
        else:
            if visited[v] == group:
                return False
    return True

for _ in range(k):
    v, e = map(int,input().split())
    g = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)
    for _ in range(e):
        a, b = map(int,input().split())
        g[a].append(b)
        g[b].append(a)
    
    for i in range(1, v + 1):
        if visited[i] == 0:
            result = dfs(i, visited, g, 1)
            if not result:
                break
    if result:
        print('YES')
    else:
        print("NO")