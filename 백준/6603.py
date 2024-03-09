import sys
input = sys.stdin.readline

answer = []

def nCr(n, ans, r, s):
    if n == len(s):
        if len(ans) == r:
            temp = [i for i in ans]
            print(" ".join(map(str,temp)))
        return
    ans.append(s[n])
    nCr(n + 1, ans, r, s)
    ans.pop()
    nCr(n + 1, ans, r, s)


while True:
    s = list(map(int,input().split()))
    if s[0] == 0:
        break
    nCr(1, [], 6, s)
    print()