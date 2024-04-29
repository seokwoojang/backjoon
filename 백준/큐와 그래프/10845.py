import sys
input = sys.stdin.readline

n = int(input())
r = []
for i in range(n):
    a = list(input().split())
    if a[0] == 'push':
        r.append(int(a[1]))
    elif a[0] == 'pop':
        if len(r) == 0:
            print(-1)
        else:
            print(r.pop(0))
    elif a[0] == 'size':
        print(len(r))
    elif a[0] == 'empty':
        if len(r) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if len(r) == 0:
            print(-1)
        else:
            print(r[0])
    elif a[0] == 'back':
        if len(r) == 0:
            print(-1)
        else:
            print(r[-1])