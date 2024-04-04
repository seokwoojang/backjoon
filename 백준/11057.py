import sys
input = sys.stdin.readline

n = int(input())

dp = [[0] * 10 for _ in range(n)]
dp[0] = [10, 9 , 8, 7, 6, 5, 4, 3, 2, 1]

for i in range(1, n):
    for j in range(10):
        if j == 0:
            dp[i][j] = (sum(dp[i-1]))%10007
        else:
            dp[i][j] = (dp[i][j-1] - dp[i-1][j-1])%10007

print(dp[n-1][0])