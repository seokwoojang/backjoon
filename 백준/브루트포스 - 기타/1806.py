import sys
input = sys.stdin.readline

n, s = map(int,input().split())
a = list(map(int,input().split()))

total = a[0]
left = 0
right = 1
minimum = 1e9

while True:
    if total < s:
        if right < n:
            total += a[right]
            right += 1
        else:
            break
    elif total >= s:
        minimum = min(right - left, minimum)
        total -= a[left]
        left += 1

if minimum == 1e9:
    print(0)
else:
    print(minimum)