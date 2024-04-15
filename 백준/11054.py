import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int,input().split()))
ra = a[::-1]
dp = [[1] * n for _ in range(2)] # 0행은 증가 / 1행은 감소

for i in range(1,n):
    for j in range(i):
        if a[i] > a[j]:
            dp[0][i] = max(dp[0][i], dp[0][j] + 1)
        if ra[i] > ra[j]:
            dp[1][i] = max(dp[1][i], dp[1][j] + 1)

result = [0] * n
for i in range(n):
    result[i] = dp[0][i] + dp[1][n-i-1]
print(max(result) - 1)