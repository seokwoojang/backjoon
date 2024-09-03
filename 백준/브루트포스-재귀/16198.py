import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
w = list(map(int,input().split()))

maxinum = -1e9

def bfs(W, total):
    global maxinum
    if len(W) == 3:
        total += (W[0] * W[2])
        maxinum = max(maxinum, total)
        return
    
    for i in range(1,len(W) - 1):
        bfs(W[:i] + W[i+1:],total + (W[i-1] * W[i+1]))


bfs(w,0)
print(maxinum)

