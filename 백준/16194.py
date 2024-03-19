import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int,input().split()))
p.insert(0,0)
dp = [100000] * (n+1)
dp[0] = 0

for i in range(1,n + 1):
    for j in range(1, i + 1):
        dp[i] = min(dp[i], p[j] + dp[i-j])

print(dp[n])