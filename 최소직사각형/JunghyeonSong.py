def solution(sizes):
    # sizes 길이가 1일 경우
    if len(sizes) < 2:
        return sizes[0][0] * sizes[0][1]
    
    # 최대 가로 길이, 최대 세로 길이
    max_w = 0
    max_h = 0   
    
    # O(N)
    for w, h in sizes:
        # 가로길이가 항상 더 길도록 회전
        if w < h:
            w, h = h, w
        
        max_w = w if w > max_w else max_w
        max_h = h if h > max_h else max_h
            
    return max_w * max_h