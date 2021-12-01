from copy import deepcopy
from collections import deque

def lotation_clock(key):
    new_key = []
    
    for i in range(len(key[0])):
        row = []
        for r in key[::-1]:
            row.append(r[i])
        new_key.append(row)
    
    return new_key
    
    
def chk_lock(lock, chk):
    flag = True
    for r in range(chk, len(lock)-chk):
        for c in range(chk, len(lock)-chk):
            if lock[r][c] != 1:
                flag = False
    return flag
    
    
def solution(key, lock):
    answer = False    
    # n = len(key)
    # m = len(lock)
    #
    # (0,0)을 기준으로 기존 lock 영역의 index 변화
    # (0,0) ~ (m-1, m-1) -> (n-1, n-1) ~ ((n-1)+(m-1), (n-1)+(m-1))
    #
    # 전체 탐색 영역의 index 변화
    # (0,0) ~ ((n-1)+(m-1), (n-1)+(m-1))
    
    # lock의 상하좌우를 len(key)-1 만큼 확장시켜 사용
    length = len(lock)+(len(key)-1)*2
    extend_lock = [[0]*length for _ in range(length)]
        
    chk = len(key)-1
    for i in range(len(lock)):
        for j in range(len(lock)):
            extend_lock[chk+i][chk+j] = lock[i][j]
    
    # 완전탐색
    for _ in range(4):
        
        for r in range(len(key)+len(lock)-1):
            for c in range(len(key)+len(lock)-1):
                extend = deepcopy(extend_lock)
                
                for i in range(len(key)):
                    for j in range(len(key[0])):
                        extend[r+i][c+j] += key[i][j]
                
                # 확장된 부분을 제외한 원래의 lock 영역만 확인
                if chk_lock(extend, chk):
                    answer = True
        
        # 회전
        key = lotation_clock(key)
        
        
    return answer
