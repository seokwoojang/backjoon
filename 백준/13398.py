import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

dp = [[0] * n for _ in range(2)]
dp[0][0] = a[0]
dp[1][0] = -1000

for j in range(1, n):
    dp[0][j] = max(dp[0][j-1] + a[j], a[j])
    dp[1][j] = max(dp[0][j-1], dp[1][j-1] + a[j])



print(max(max(dp[0]),max(dp[1])))