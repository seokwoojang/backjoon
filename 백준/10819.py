import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
visit = n * [0]

maxnum = 0
s = []

def dfs():
    global maxnum
    if len(s) == n:
        r = 0
        for i in range(n-1):
            r += abs(s[i] - s[i+1])
        maxnum = max(r, maxnum)
        return
    
    for i in range(n):
        if not visit[i]:
            visit[i] = 1
            s.append(a[i])
            dfs()
            visit[i] = 0
            s.pop()

dfs()
print(maxnum)