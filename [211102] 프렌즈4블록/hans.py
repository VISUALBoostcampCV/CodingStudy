def solution(m, n, board):
    answer = 0
    delete = set()
    square = [(0,0),(1,0),(0,1),(1,1)]
    board_list = [list(b) for b in board]
    
    while True:
        for y in range(m-1):
            for x in range(n-1):
                sample = board_list[y][x]
                if sample=='.':
                    continue
                for m_x, m_y in square:
                    new_x, new_y = x+m_x, y+m_y
                    if board_list[new_y][new_x]!=sample:
                        break
                else:
                    delete.update([(y+j,x+i) for i,j in square])
        for d_y, d_x in delete:
            board_list[d_y][d_x]='.'
        for x in range(n):
            lst = [board_list[y][x] for y in range(m-1,-1,-1) if board_list[y][x]!='.']
            lst += ['.' for i in range(m-len(lst))]
            for y in range(m):
                board_list[y][x]=lst.pop()
                
        if len(delete)==0:
            break
        answer += len(delete)
        delete.clear()
    
    return answer


'''
테스트 1 〉	통과 (0.06ms, 10.3MB)
테스트 2 〉	통과 (0.08ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (1.69ms, 10.3MB)
테스트 5 〉	통과 (90.86ms, 10.3MB)
테스트 6 〉	통과 (7.96ms, 10.3MB)
테스트 7 〉	통과 (1.15ms, 10.4MB)
테스트 8 〉	통과 (1.42ms, 10.4MB)
테스트 9 〉	통과 (0.08ms, 10.4MB)
테스트 10 〉	통과 (0.85ms, 10.3MB)
테스트 11 〉	통과 (3.44ms, 10.3MB)

'''