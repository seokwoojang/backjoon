import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j] :
            dp[i] = max(dp[j] + 1, dp[i])
print(max(dp))

cnt = max(dp)
r = []
for i in range(n-1,-1,-1):
    if dp[i] == cnt:
        cnt -= 1
        r.append(a[i])
r.reverse()
print