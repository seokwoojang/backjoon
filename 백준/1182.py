import sys
input = sys.stdin.readline

n, s = map(int,input().split())

l = list(map(int,input().split()))

count = 0

def combi(n, ans):
    global count
    if n == len(l):
        temp = [i for i in ans]
        if sum(temp) == s and len(temp)>0:
            count = count + 1
        return
    
    ans.append(l[n])
    combi(n + 1, ans)
    ans.pop()
    combi(n + 1, ans)

combi(0, [])
print(count)
