from functools import reduce
def rotate(m, d):
    if d==0:
        return m
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if d==90:
                ret[c][N-1-r] = m[r][c]
            elif d==180:
                ret[N-1-r][N-1-c] = m[r][c]
            elif d==270:
                ret[N-1-c][r] = m[r][c]
                
    return ret

def solution(key, lock):
    answer = 0
    N,M = len(lock),len(key)
    r = [90, 180, 270, 0]
    n_hole = reduce(lambda x, y: x+y.count(0), lock, 0) # 홈 개수
    
    for d in r:
        new_key = rotate(key, d)
        miss = 0
        for l_y in range(-N+1,N):
            for l_x in range(-N+1,N):
                fill = 0
                flag = False
                for k_y in range(M):
                    for k_x in range(M):
                        y,x = l_y+k_y, l_x+k_x
                        if y < 0 or x<0 or y>=N or x>=N:
                            continue
                        if new_key[k_y][k_x] and lock[y][x]==0:
                            fill+=1
                        elif new_key[k_y][k_x] and lock[y][x]:
                            flag = True
                            break
                    if flag: break
                else:
                    if fill==n_hole:
                        return True
            
    return False

'''
테스트 1 〉	통과 (0.19ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.98ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (2.43ms, 10.3MB)
테스트 6 〉	통과 (5.48ms, 10.3MB)
테스트 7 〉	통과 (31.49ms, 10.3MB)
테스트 8 〉	통과 (5.81ms, 10.3MB)
테스트 9 〉	통과 (7.48ms, 10.3MB)
테스트 10 〉	통과 (16.65ms, 10.3MB)
테스트 11 〉	통과 (29.53ms, 10.4MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.60ms, 10.4MB)
테스트 14 〉	통과 (0.22ms, 10.3MB)
테스트 15 〉	통과 (1.02ms, 10.2MB)
테스트 16 〉	통과 (3.43ms, 10.4MB)
테스트 17 〉	통과 (11.81ms, 10.3MB)
테스트 18 〉	통과 (4.12ms, 10.3MB)
테스트 19 〉	통과 (0.24ms, 10.3MB)
테스트 20 〉	통과 (18.51ms, 10.3MB)
테스트 21 〉	통과 (35.02ms, 10.4MB)
테스트 22 〉	통과 (4.32ms, 10.3MB)
테스트 23 〉	통과 (0.85ms, 10.3MB)
테스트 24 〉	통과 (1.01ms, 10.4MB)
테스트 25 〉	통과 (33.60ms, 10.3MB)
테스트 26 〉	통과 (21.90ms, 10.3MB)
테스트 27 〉	통과 (42.36ms, 10.2MB)
테스트 28 〉	통과 (2.98ms, 10.3MB)
테스트 29 〉	통과 (1.71ms, 10.3MB)
테스트 30 〉	통과 (4.37ms, 10.3MB)
테스트 31 〉	통과 (18.20ms, 10.3MB)
테스트 32 〉	통과 (40.81ms, 10.3MB)
테스트 33 〉	통과 (5.56ms, 10.3MB)
테스트 34 〉	통과 (0.55ms, 10.3MB)
테스트 35 〉	통과 (0.38ms, 10.4MB)
테스트 36 〉	통과 (0.71ms, 10.3MB)
테스트 37 〉	통과 (0.44ms, 10.3MB)
테스트 38 〉	통과 (0.22ms, 10.2MB)

'''