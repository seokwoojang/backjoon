import sys
input = sys.stdin.readline

n = int(input())
w = list(map(int,input().split()))

maxinum = -1e9

def bt(W, total):
    global maxinum
    if len(W) == 3:
        total += (W[0] * W[2])
        maxinum = max(maxinum, total)
        return
    
    for i in range(1,len(W) - 1):
        bt(W[:i] + W[i+1:],total + (W[i-1] * W[i+1]))


bt(w,0)
print(maxinum)

