import sys
input = sys.stdin.readline

n = int(input())

primeArr = [False,False]+[True]*(n-1)

for i in range(2,n+1):
    if primeArr[i]:
        for j in range(i*2, n+1 ,i):
            primeArr[j]=False

total = 2
left = 2
right = 3
cnt = 0

if n == 1:
    print(0)
    exit()

while True:
    if total < n:
        if right <= n :
            if primeArr[right]:
                total += right
                right += 1
            else:
                right += 1
        else:
            break
    elif total == n and primeArr[left]:
        cnt += 1
        total -= left
        left += 1
    else:
        if primeArr[left]:
            total -= left
            left += 1
        else:
            left += 1


print(cnt)