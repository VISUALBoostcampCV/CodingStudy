import numpy as np
from collections import deque
def solution(key, lock):
    N = len(key)
    answer = False
    mat = np.pad(lock, N - 1)
    
    q = deque([(0, 0)])
    visited = []
    while q:
        cur_row, cur_col = q.popleft()
        if (cur_row, cur_col) in visited:
            continue
        # 키 넣어보기
        for K in range(1, 4):
            mat[cur_row:cur_row+N, cur_col:cur_col+N] += np.rot90(key, k=K)
            # 키가 맞으면 return
            if np.max(mat[N-1:N*2-1, N-1:N*2-1]) == 1 and np.min(mat[N-1:N*2-1, N-1:N*2-1]) == 1:
                return True
        # 키가 안맞으면 다음 위치 추가
        for d_row, d_col in [(1, 0), (0, 1)]:
            if cur_row + d_row >= len(mat) - 1 or cur_col + d_col >= len(mat[0]):
                continue
            q.append((cur_row + d_row, cur_col + d_col))
            visited.append((cur_row, cur_col))
    return answer

solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])

# # 이전 풀이
# def attach(x, y, m, key, figure):
#     for i in range(m):
#         for j in range(m):
#             figure[x + i][y + j] += key[i][j]

# def detach(x, y, m, key, figure):
#     for i in range(m):
#         for j in range(m):
#             figure[x + i][y + j] -= key[i][j]

# def check(figure, m, n):
#     for i in range(n):
#         for j in range(n):
#             if figure[m + i][m + j] != 1:
#                 return False
#     return True

# def rotate(key):
#     return list(zip(*key[::-1]))

# def solution(key, lock):
#     m, n = len(key), len(lock)

#     figure = [[0] * (2 * m + n) for _ in range(m * 2 + n)]

#     for i in range(n):
#         for j in range(n):
#             figure[m + i][m + j] = lock[i][j]

#     rotated_key = key
#     for _ in range(4):
#         rotated_key = rotate(rotated_key)
#         for x in range(1, m + n):
#             for y in range(1, m + n):
#                 attach(x, y, m, rotated_key, figure)
#                 if check(figure, m, n):
#                     return True
#                 detach(x, y, m, rotated_key, figure)
#     return False