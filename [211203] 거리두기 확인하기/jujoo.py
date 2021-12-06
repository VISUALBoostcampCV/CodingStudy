def solution(places):
    answer = []
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for n, place in enumerate(places):
        for row in range(5):
            if len(answer) == n + 1:
                break
            for col in range(5):
                # 현재 위치가 O면 상하좌우에 P가 2개 이상이면 안됨
                if place[row][col] == 'O':
                    cnt = 0
                    for d_row, d_col in d:
                        nxt_row, nxt_col = row + d_row, col + d_col
                        if nxt_row < 0 or nxt_row >= 5 or nxt_col < 0 or nxt_col >= 5:
                            continue
                        if place[nxt_row][nxt_col] == 'P':
                            cnt += 1
                    if cnt > 1:
                        answer.append(0)
                        break
                # 현재 위치가 p면 상하좌우에 p가 없어야함
                if place[row][col] == 'P':
                    flag = False
                    for d_row, d_col in d:
                        nxt_row, nxt_col = row + d_row, col + d_col
                        if nxt_row < 0 or nxt_row >= 5 or nxt_col < 0 or nxt_col >= 5:
                            continue
                        if place[nxt_row][nxt_col] == 'P':
                            answer.append(0)
                            flag = True
                            break
                    if flag:
                        break
        else:
            answer.append(1)
            
    return answer