# O(n)
from typing import List
def solution(sizes : List[List[int]]) -> int:
    # 지갑 사이즈
    w_max, h_max = 0, 0

    for w, h in sizes:
        # 세로 길이가 더 길면 회전 -> 가로 길이가 긴 명함으로 통일
        if w < h:
            w, h = h, w
        # 가로, 세로 길이의 최댓값을 update
        w_max = max(w_max, w)
        h_max = max(h_max, h)
    return w_max * h_max