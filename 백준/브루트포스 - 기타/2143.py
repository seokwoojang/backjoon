from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

aSum = []
bSum = []

for i in range(n):
    for j in range(i + 1, n + 1):
        aSum.append(sum(A[i:j]))
for i in range(m):
    for j in range(i + 1, m + 1):
        bSum.append(sum(B[i:j]))

aSum.sort()
bSum.sort()

ans = 0
for i in range(len(aSum)):
    bmp = T - aSum[i]
    left = bisect_left(bSum, bmp)
    right = bisect_right(bSum, bmp)
    ans += (right - left)
print(ans)