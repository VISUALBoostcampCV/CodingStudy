def check(i,j,b):
    if b[i][j] != " " and b[i][j] == b[i+1][j] and b[i][j] == b[i][j+1] and b[i][j] == b[i+1][j+1]:
        return 1
    else: 
        return 0
    
def delete(clear, b):
    for (i,j) in clear:
        b[i][j] = " "
        b[i][j+1] = " "
        b[i+1][j] = " "
        b[i+1][j+1] = " "  

def down(m,j,b):
    for i in range(0,m):
        if b[i][j] == " ":
            for k in range(0, i):
                b[i-k][j] = b[i-1-k][j]
            b[0][j] = " "        
            
def solution(m, n, board):
    b = []
    for i in range(0,m):
        b.append((list(board[i])))
        
    while True:
        clear=[]
        for i in range(0,m-1):
            for j in range(0,n-1):
                if check(i,j,b):
                    clear.append([i,j])
                    
        delete(clear, b)
        
        for j in range(0,n):
            down(m,j,b)
                    
        if len(clear) == 0:
            break
            
    answer = 0
    for i in range(0,m):
        answer+=b[i].count(" ")
    return answer



'''
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.06ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (3.69ms, 10.3MB)
테스트 5 〉	통과 (211.76ms, 10.3MB)
테스트 6 〉	통과 (14.25ms, 10.3MB)
테스트 7 〉	통과 (1.90ms, 10.3MB)
테스트 8 〉	통과 (3.72ms, 10.4MB)
테스트 9 〉	통과 (0.04ms, 10.3MB)
테스트 10 〉	통과 (1.32ms, 10.4MB)
테스트 11 〉	통과 (6.71ms, 10.3MB)
'''