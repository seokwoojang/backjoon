import sys
input = sys.stdin.readline

dp = [1, 2, 4, 7]
for i in range(int(input())):
    n = int(input())
    for i in range(len(dp),n):
        dp.append((dp[i-1] + dp[i-2] + dp[i-3])%1000000009)
    print(dp[n-1])