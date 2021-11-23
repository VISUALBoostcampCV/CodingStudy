# -- 1
import numpy as np
def solution(m:int, n:int, board:list)->int:
    board = np.array(list(map(list, board)))
    cnt = 0
    while True:
        visited = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == ' ':
                    continue
                if board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
                    visited |= {(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)}
        if not visited:
            break
        board = arrange(board, visited)
        cnt += len(visited)
    return cnt
        
def arrange(board:np.array, visited:set)->list:
    for row, col in visited:
        board[row][col] = ' '

    new_board = []
    for col in range(len(board[0])):
        cur_col = board[:, col]
        idx = np.where(board[:, col] != ' ')[0]
        new_board.append(([' '] * (len(cur_col) - len(idx)) + list(cur_col[idx])))
    return np.stack(new_board, 1)

# 테스트 1 〉	통과 (0.20ms, 28MB)
# 테스트 2 〉	통과 (0.30ms, 27.9MB)
# 테스트 3 〉	통과 (0.10ms, 27.9MB)
# 테스트 4 〉	통과 (3.56ms, 28.1MB)
# 테스트 5 〉	통과 (252.85ms, 27.9MB)
# 테스트 6 〉	통과 (21.38ms, 27.7MB)
# 테스트 7 〉	통과 (4.37ms, 27.9MB)
# 테스트 8 〉	통과 (3.43ms, 27.9MB)
# 테스트 9 〉	통과 (0.21ms, 28MB)
# 테스트 10 〉	통과 (2.22ms, 27.8MB)
# 테스트 11 〉	통과 (4.50ms, 27.8MB)

# -- 2
def pang(arr:list, m:int, n:int, cnt:int)->(list, int):
    idx_set = set()
    for i in range(m - 1):
        for j in range(n - 1):
            if arr[i][j] == arr[i + 1][j + 1] == arr[i + 1][j] == arr[i][j + 1] != "0":
                idx_set |= {(i, j), (i + 1, j + 1), (i + 1, j), (i, j + 1)}

    if not idx_set:
        return arr, 0
    cnt += len(idx_set)

    for i, j in idx_set:
        arr[i][j] = "0"
    return arr, cnt

def dropthearray(arr:list)->list:
    for _ in range(len(arr)):
        for i in range(len(arr) - 1):
            for idx, (a, b) in enumerate(list(zip(arr[i], arr[i + 1]))):
                if b == "0":
                    arr[i][idx], arr[i + 1][idx] = arr[i + 1][idx], arr[i][idx]
    return arr

def solution(m:int, n:int, board:list)->int:
    arr = list(map(list, board))
    cnt = 0
    while True:
        arr, a = pang(arr, m, n, 0)
        if a == 0:
            return cnt
        cnt += a
        arr = dropthearray(arr)

# 테스트 1 〉	통과 (0.09ms, 10.3MB)
# 테스트 2 〉	통과 (0.10ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (7.89ms, 10.4MB)
# 테스트 5 〉	통과 (942.15ms, 10.4MB)
# 테스트 6 〉	통과 (64.37ms, 10.3MB)
# 테스트 7 〉	통과 (3.12ms, 10.4MB)
# 테스트 8 〉	통과 (7.72ms, 10.3MB)
# 테스트 9 〉	통과 (0.05ms, 10.3MB)
# 테스트 10 〉	통과 (4.98ms, 10.3MB)
# 테스트 11 〉	통과 (19.13ms, 10.4MB)