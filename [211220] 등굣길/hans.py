



'''
# old code
def solution(m, n, puddles):
    board = [[0] * (m+1) for _ in range(n+1)]
    for x,y in puddles:
        board[y][x] = -1
    board[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if board[i][j] == -1:
                board[i][j] = 0
                continue
            
            board[i][j] += (board[i-1][j] + board[i][j-1]) % 1000000007
        #print(board[i][j])
    #print(board)
    return board[n][m]

테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.1MB)
테스트 5 〉	통과 (0.07ms, 10.3MB)
테스트 6 〉	통과 (0.05ms, 10.2MB)
테스트 7 〉	통과 (0.05ms, 10.2MB)
테스트 8 〉	통과 (0.11ms, 10.2MB)
테스트 9 〉	통과 (0.06ms, 10.2MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (2.58ms, 10.3MB)
테스트 2 〉	통과 (1.34ms, 10.2MB)
테스트 3 〉	통과 (1.50ms, 10.3MB)
테스트 4 〉	통과 (2.08ms, 10.3MB)
테스트 5 〉	통과 (1.98ms, 10.4MB)
테스트 6 〉	통과 (2.66ms, 10.4MB)
테스트 7 〉	통과 (1.46ms, 10.3MB)
테스트 8 〉	통과 (2.07ms, 10.4MB)
테스트 9 〉	통과 (2.15ms, 10.3MB)
테스트 10 〉	통과 (2.16ms, 10.3MB)
'''