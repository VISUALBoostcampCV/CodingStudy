def solution(grid):
    answer = []
    
    if len(grid) == 1:
        return [1, 1, 1, 1]
    
    
    visit_check = []
    is_two_dim = len(grid[0]) > 1
    size = (len(grid), len(grid[0])) if is_two_dim else len(grid)
    make_list(visit_check, size, is_two_dim)
    
    # 진행방향 인덱스. 2차원 리스트일때 사용
    up = (-1, 0)
    down = (1, 0)
    left = (0, -1)
    right = (0, 1)
    
    # 이전 진행방향: 다음 갈 곳
    light_dict = {
                    'up': {'S': up, 'L': left, 'R': right},
                    'down': {'S': down, 'L': right, 'R': left},
                    'left': {'S': left, 'L': down, 'R': up},
                    'right': {'S': right, 'L': up, 'R': down}
                 }
    
    index = None
    prv_d = ''
    nxt_d = ''
    
    def go_light():
        return index + light_dict[prv_d][nxt_d]
    
    # 순환경로 탐색
    if is_two_dim:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                continue
    else:
        for i in range(len(grid)):
            continue
            
    return answer
    

def make_list(lst, size, is_two_dim):
    if is_two_dim:
        row, col = size
        for r in range(row):        
            lst.append([0 for c in range(col)])
    else:
        for s in range(size):        
            lst.append(0)

def clean_list(lst, size, is_two_dim):
    if is_two_dim:
        row, col = size
        for r in range(row):        
            for c in range(col):
                lst[r][c] = 0
    else:
        for s in range(size):        
            lst[s] = 0