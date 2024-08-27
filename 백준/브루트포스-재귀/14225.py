import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int,input().split()))

answer_list = []

def combi(n, ans):

    if n == len(s):
        temp = 0
        for i in range(len(ans)):
            temp += ans[i]
        answer_list.append(temp)
        return
    ans.append(s[n])
    combi(n + 1, ans)
    ans.pop()
    combi(n + 1, ans)

combi(0, [])
answer_list.sort()
answer_list = list(set(answer_list))

for i in range(len(answer_list)):
    if i != answer_list[i]:
        print(i)
        exit()

print(len(answer_list))