def solution(rectangle, characterX, characterY, itemX, itemY):
    # 최소 좌표평면 만들기
    board_len = max([max(coordinates) for coordinates in zip(*rectangle)]) * 2 + 1
    board = [[0 for y in range(board_len)] for x in range(board_len)]
    path = [[float('inf') for y in range(board_len)] for x in range(board_len)]
    
    # 직사각형 테두리는 1, 면은 0으로 채우기
    for rec in rectangle:
        l_x, l_y, r_x, r_y = list(map(lambda x: x * 2, rec))
        
        for x in range(l_x, r_x):
            for y in range(l_y, r_y):
                board[x][y] = 1
        
        for x in range(l_x + 1, r_x - 1):
            for y in range(l_y + 1, r_y - 1):
                board[x][y] = 0
    
    cx = characterX * 2
    cy = characterY * 2
    ix = itemX * 2
    iy = itemY * 2
    
    # 캐릭터가 이동 가능한 경로 길이 재기
    path[cx][cy] = 0
    move((cx, cy), (ix, iy), board, path)
    
    return path[ix][iy] // 2


# 좌표 평면 범위인지 확인해주는 함수
def is_in_board(x, y, board_len):
    return x > 0 and x < board_len and y > 0 and y < board_len


# 테두리 따라 이동하는 함수
def move(start, end, board, path):
    direct = ((0, -1), (0, 1), (-1, 0), (1, 0))
    board_len = len(board)
    x, y = start
    
    for _x, _y in direct:
        _x += x
        _y += y
        
        # 좌표 평면에서 벗어나는 경우
        if not is_in_board(_x, _y, board_len):
            continue
        
        # 도착한 경우
        if _x == end[0] and _y == end[1]:            
            path[_x][_y] = min(path[_x][_y], 1 + path[x][y])
            return
        
        # 아직 방문하지 않았거나 더 긴 경로인 테두리인 경우
        next_path = 1 + path[x][y]
        if board[_x][_y] and path[_x][_y] > next_path:
            path[_x][_y] = next_path
            move((_x, _y), end, board, path)
    
    return