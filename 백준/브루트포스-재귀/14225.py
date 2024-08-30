import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int,input().split()))

answer = []

def combi(n,ans):
    if n == len(s):
        temp = 0
        for i in range(len(ans)):
            temp += ans[i]
        answer.append(temp)
        return 

    ans.append(s[n])
    combi(n+1, ans)
    ans.pop()
    combi(n+1, ans)
    

combi(0,[])
answer.sort()
answer = list(set(answer))

for i in range(len(answer)):
    if i != answer[i]:
        print(i)
        exit()

print(len(answer))