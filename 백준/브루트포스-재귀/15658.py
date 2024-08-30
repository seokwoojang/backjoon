import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
o = list(map(int,input().split()))

maximum = -1e9
minimum = 1e9

def dfs(depth, total, plus, minus, multiple, division) :
    global maximum,minimum
    if depth == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
    
    if depth < n:
        if plus:
            dfs(depth + 1, total + a[depth], plus - 1, minus, multiple, division)
        if minus :
            dfs(depth + 1, total - a[depth], plus, minus - 1, multiple, division)
        if multiple:
            dfs(depth + 1, total * a[depth], plus, minus, multiple - 1, division)
        if division:
            dfs(depth + 1, int(total / a[depth]), plus, minus, multiple, division - 1)
        
    

dfs(1,a[0],o[0],o[1],o[2],o[3])
print(maximum)
print(minimum)