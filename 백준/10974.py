import sys
input = sys.stdin.readline

N = int(input())
s = []

def dfs():
    if len(s) == N:
        print(" ".join(map(str,s)))
        return
    
    for i in range(N):
        if i+1 in s:
            continue
        s.append(i+1)
        dfs()
        s.pop()

dfs()