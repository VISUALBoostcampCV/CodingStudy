def solution(grid):

    ## 노드이름과 빛이 들어오는 방향을 확인하고 
    ## 빛이 나가는 방향을 return 
    def get_out(node, inn):
        if node == 'S':
            if inn == 'u': out = 'd'
            elif inn == 'd': out = 'u'
            elif inn == 'r': out = 'l'
            else: out = 'r'
            
        elif node =='L':
            if inn =='u': out = 'l'
            elif inn == 'd': out = 'r'
            elif inn == 'r': out = 'u'
            else: out = 'd'
        else:
            if inn =='u': out = 'r'
            elif inn == 'd': out = 'l'
            elif inn == 'r': out = 'd'
            else: out = 'u'
        
        if check[row][col][W[out]]:
            return '0'
        check[row][col][W[out]] = True
        return out
    
    ## 빛이 나가는 방향을 확인하고 
    ## 다음 노드위치와 다음 노드한테 들어가는 빛의 방향 return
    def get_next(row, col, out):
        if out =='r':
            if col == len(grid[0])-1: col = 0
            else: col+=1
            inn = 'l'
        elif out =='l':
            if col == 0: col = len(grid[0])-1
            else: col-=1
            inn = 'r'
        elif out=='u':
            if row == 0: row = len(grid)-1
            else: row-=1
            inn = 'd'
        else:
            if row == len(grid)-1: row=0
            else: row+=1
            inn = 'u'
        return row, col, inn
            
    W = {'u':0, 'l':1, 'd':2, 'r':3}
    answer = []
    check=[]

    # 빛이 나갔는지 체크
    for _ in range(len(grid)):
        c = [[False] * 4 for _ in range(len(grid[0]))]
        check.append(c)
    
    ## 모든 노드 확인하긴하는데
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            ## 그 노드에 빛이 나가지 않은 곳이 있으면
            if not all(check[row][col]):
                ## 모든 방향에서 빛 쏘기
                for i in range(4):
                    inn = list(W.keys())[i]
                    cnt=0
                    while True:
                        node = grid[row][col]
                        out = get_out(node, inn)
                        if out =='0':
                            break
                        cnt+=1
                        row,col,inn = get_next(row,col,out)

                    if cnt!=0:
                        answer.append(cnt)

    return sorted(answer)

'''
정확성  테스트
테스트 1 〉	통과 (0.24ms, 10.3MB)
테스트 2 〉	통과 (0.45ms, 10.4MB)
테스트 3 〉	통과 (0.51ms, 10.3MB)
테스트 4 〉	통과 (22.67ms, 10.7MB)
테스트 5 〉	통과 (44.08ms, 11.4MB)
테스트 6 〉	통과 (48.04ms, 11.8MB)
테스트 7 〉	통과 (662.44ms, 32.4MB)
테스트 8 〉	통과 (568.22ms, 29.7MB)
테스트 9 〉	통과 (998.51ms, 34.6MB)
테스트 10 〉	통과 (1158.28ms, 40MB)
테스트 11 〉	통과 (1320.41ms, 41.6MB)
'''