def solution(key, lock):
    M = len(key)
    N = len(lock)        
    
    ## 회전시키기
    def turn90(old_key):
        new_key=[[0]*M for _ in range(M)]
        for i in range(M):
            for j in range(M):
                new_key[j][M-1-i] = old_key[i][j]
        return new_key
    
    ## 빈 행렬에 key 넣어주기
    def ff(test, key, starti, startj):
        for i in range(M):
            for j in range(M):
                test[starti+i][startj+j] = key[i][j]
                
    ## lock에 맞는 key인지 확인
    def check(key, lock):
        for i in range(len(key)):
            for j in range(len(key)):
                if key[i][j]^lock[i][j]:
                    continue
                else:
                    return False
        return True
    
    ## 90, 180, 270, 360 돌리기
    for _ in range(4):
        key = turn90(key)

        ## 빈 행렬에 넣고 잘라서 확인해보기
        for i in range(0, N+M-1):
            for j in range(0, N+M-1):
                test_key = [[0]*(N+2*(M-1)) for _ in range((N+2*(M-1)))]
                ff(test_key, key, i, j)
                
                n_key = [[0]*N for _ in range(N)]

                ## 넣어진 key 행렬 lock크기만큼 자르기
                for k in range(M-1, N+M-1):
                    n_key[k-(M-1)][:] = test_key[k][M-1:N+M-1]

                # lock에 맞는 key면 바로 true 반환
                if check(n_key, lock):
                    return True

    return False

'''
정확성  테스트
테스트 1 〉	통과 (0.59ms, 10.3MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
테스트 3 〉	통과 (6.46ms, 10.3MB)
테스트 4 〉	통과 (0.12ms, 10.2MB)
테스트 5 〉	통과 (17.00ms, 10.4MB)
테스트 6 〉	통과 (15.73ms, 10.3MB)
테스트 7 〉	통과 (139.21ms, 10.4MB)
테스트 8 〉	통과 (39.82ms, 10.3MB)
테스트 9 〉	통과 (45.99ms, 10.3MB)
테스트 10 〉	통과 (115.48ms, 10.3MB)
테스트 11 〉	통과 (209.05ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (2.35ms, 10.3MB)
테스트 14 〉	통과 (0.80ms, 10.2MB)
테스트 15 〉	통과 (4.83ms, 10.3MB)
테스트 16 〉	통과 (25.53ms, 10.3MB)
테스트 17 〉	통과 (55.23ms, 10.4MB)
테스트 18 〉	통과 (17.57ms, 10.3MB)
테스트 19 〉	통과 (0.56ms, 10.3MB)
테스트 20 〉	통과 (64.64ms, 10.4MB)
테스트 21 〉	통과 (122.17ms, 10.3MB)
테스트 22 〉	통과 (19.13ms, 10.4MB)
테스트 23 〉	통과 (3.82ms, 10.3MB)
테스트 24 〉	통과 (4.03ms, 10.4MB)
테스트 25 〉	통과 (149.24ms, 10.3MB)
테스트 26 〉	통과 (166.76ms, 10.3MB)
테스트 27 〉	통과 (309.71ms, 10.3MB)
테스트 28 〉	통과 (21.19ms, 10.2MB)
테스트 29 〉	통과 (7.46ms, 10.3MB)
테스트 30 〉	통과 (34.07ms, 10.4MB)
테스트 31 〉	통과 (75.41ms, 10.3MB)
테스트 32 〉	통과 (146.72ms, 10.3MB)
테스트 33 〉	통과 (30.33ms, 10.3MB)
테스트 34 〉	통과 (2.38ms, 10.3MB)
테스트 35 〉	통과 (2.34ms, 10.3MB)
테스트 36 〉	통과 (3.57ms, 10.3MB)
테스트 37 〉	통과 (2.13ms, 10.2MB)
테스트 38 〉	통과 (0.54ms, 10.3MB)
'''