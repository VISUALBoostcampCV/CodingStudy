
def solution(places):
    answer = []
    
    for place in places:
        
        # 2x2 박스 탐색
        # p가 2개일때
        geori = 1
        for r in range(4):
            for c in range(4):
                if not geori:
                    break
                row1 = [place[r][c], place[r][c+1]]
                row2 = [place[r+1][c], place[r+1][c+1]]
                
                # P가 좌우로 붙어있는 경우
                if row1.count('P') == 2 or row2.count('P') == 2:
                    geori = 0
                    
                elif row1.count('P') + row2.count('P') == 2:
                    # P가 상하로 붙어있는 경우
                    if row1.index('P') == row2.index('P'):
                        geori = 0
                    # P가 대각선으로 위치하는 경우
                    if row1.count('O') or row2.count('O'):
                        geori = 0
        
        # P가 3개 일때
        # 전치행렬 사용하여 가로로 POP 세로로 POP 한번에 탐색
        place2 = [''.join(x) for x in zip(*place)] # place의 전치행렬
        for r in range(5):
            for c in range(3):
                if not geori:
                    break
                row1 = place[r][c:c+3] # 가로 POP
                row2 = place2[r][c:c+3] # 세로 POP
                
                if row1 == 'POP' or row2 == 'POP':
                    geori = 0
                
        answer.append(geori)
    
    return answer
