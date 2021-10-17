# <--in progress-->
import numpy as np
def solution(line):
    arr = np.array(line, dtype=np.int64)
    pt = []
    
    left = arr[:, :2]
    right = arr[:, -1] * -1
    x_min, y_min, x_max, y_max = 1000, 1000, 0, 0
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            try:
                inv = np.linalg.inv(left[[i, j]]) # 역행렬
            except:
                continue
            x, y = np.matmul(inv, right[[i, j]])
            if x == int(x) and y == int(y):
                pt.append((x, y))
                x_min, x_max = min(x_min, x), max(x_max, x)
                y_min, y_max = min(y_min, y), max(y_max, y)
    
    row, col = y_max - y_min, x_max - m_min