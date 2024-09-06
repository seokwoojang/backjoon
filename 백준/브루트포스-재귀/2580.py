import sys
input = sys.stdin.readline

def check_col(n, y):
    for i in range(9):
        if sudoku[i][y] == n:
            return False
    return True

def check_row(n, x):
    for i in range(9):
        if sudoku[x][i] == n:
            return False
    return True

def check_matrix(x,y,n):
    x = x // 3 * 3
    y = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if sudoku[x + i][y + j] == n:
                return False
    return True

def dfs(cnt):
    if cnt == len(zero):
        for i in range(9):
            print(*sudoku[i])
        exit()
    
    x = zero[cnt][0]
    y = zero[cnt][1]

    for i in range(1,10):
        if check_col(i, y) and check_row(i, x) and check_matrix(x, y, i):
            sudoku[x][y] = i
            dfs(cnt + 1)
            sudoku[x][y] = 0

sudoku = []
for i in range(9):
    sudoku.append(list(map(int,input().split())))

zero = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zero.append([i,j])

print("---------------------------------------")
dfs(0)
