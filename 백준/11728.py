import sys
input = sys.stdin.readline

m = int(input())
s = set()

for i in range(m):
    a = input().strip().split()

    if len(a) == 1:
        if a[0] == 'all':
            s = set([i for i in range(1,21)])
        else:
            s = set()
        continue 

    command, b = a[0], a[1]
    b = int(b)

    if command == 'add':
        s.add(b)
    elif command == 'check':
        if b in s:
            print(1)
        else:
            print(0)
    elif command == "remove":
        s.discard(b)
    elif command == 'toggle':
        if b in s:
            s.discard(b)
        else:
            s.add(b)