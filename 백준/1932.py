import sys
input = sys.stdin.readline

n = int(input())
t = [[0] * 500 for _ in range(500)]

for i in range(n):
    t[i] = list(map(int, input().split()))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            t[i][j] = t[i-1][j] + t[i][j]
        elif j == i:
            t[i][j] = t[i-1][j-1] + t[i][j]
        else:
            t[i][j] = max(t[i-1][j-1], t[i-1][j]) + t[i][j]

print(max(t[n-1]))