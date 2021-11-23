def solution(m, n, board):
    answer = 0
    
    # b = list(map(list,zip(*board)))
    
    # ["TTTANT",         ['TTTRRT', 
    #  "RRFACC",          'MTRRRT', 
    #  "RRRFCC",          'MMRRFT', 
    #  "TRRRAA",    ==>   'TMRFAA', 
    #  "TTMMMF",          'TMACCN', 
    #  "TMMTTJ"]          'JFACCT']
    
    lst = []
    for j in range(n):
        tmp = ''
        for i in range(m, 0, -1):
            tmp += board[i-1][j]
        lst.append(tmp)
    
    deletes = {1}
    while deletes:
        deletes.clear()
        
        for i in range(len(lst)):
            for j in range(len(lst[i])):
                if j+1 >= len(lst[i]) or i+1>=len(lst) or j+1>=len(lst[i+1]):
                    continue
                if lst[i][j] == lst[i][j+1] == lst[i+1][j] == lst[i+1][j+1]:
                    deletes.add((i  ,j))
                    deletes.add((i  ,j+1))
                    deletes.add((i+1,j))
                    deletes.add((i+1,j+1))
        # print(deletes)
        for i in range(len(lst)):
            tmp = ''
            for j in range(len(lst[i])):
                if (i,j) in deletes:
                    answer +=1
                    continue
                tmp+=lst[i][j]
            lst[i] = tmp            

    return answer
