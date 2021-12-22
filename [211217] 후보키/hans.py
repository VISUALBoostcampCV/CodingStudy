
from itertools import combinations
def solution(relation):
    row = len(relation)
    col = len(relation[0])
    
    comb = []
    for c in range(col):
        comb.extend(combinations(range(col), c+1))      # 모든 조합
        
    unique = []
    for com in comb:
        tmp2 = []
        for i in range(row):                            # 유일성 검사
            tmp = []
            for c in com:
                tmp.append(relation[i][c])
            if tmp not in tmp2:
                tmp2.append(tmp)
            else:
                break
        else:                                           # 유일성 통과, 최소성 거사
            for i in unique:
                if set(i).issubset(set(com)):
                    break
            else:
                unique.append(com)                      # 최소성 통과
    
    return len(unique)

    '''
테스트 1 〉	통과 (0.04ms, 27.7MB)
테스트 2 〉	통과 (0.06ms, 27.8MB)
테스트 3 〉	통과 (0.06ms, 27.9MB)
테스트 4 〉	통과 (0.03ms, 27.7MB)
테스트 5 〉	통과 (0.03ms, 27.9MB)
테스트 6 〉	통과 (0.01ms, 27.9MB)
테스트 7 〉	통과 (0.02ms, 27.8MB)
테스트 8 〉	통과 (0.01ms, 27.8MB)
테스트 9 〉	통과 (0.08ms, 27.8MB)
테스트 10 〉	통과 (0.09ms, 27.9MB)
테스트 11 〉	통과 (0.15ms, 27.9MB)
테스트 12 〉	통과 (0.75ms, 27.9MB)
테스트 13 〉	통과 (0.25ms, 27.9MB)
테스트 14 〉	통과 (0.06ms, 27.7MB)
테스트 15 〉	통과 (0.03ms, 27.9MB)
테스트 16 〉	통과 (0.04ms, 27.8MB)
테스트 17 〉	통과 (0.04ms, 27.9MB)
테스트 18 〉	통과 (3.40ms, 27.8MB)
테스트 19 〉	통과 (1.54ms, 28MB)
테스트 20 〉	통과 (3.14ms, 27.9MB)
테스트 21 〉	통과 (0.68ms, 27.9MB)
테스트 22 〉	통과 (0.73ms, 27.8MB)
테스트 23 〉	통과 (0.05ms, 27.8MB)
테스트 24 〉	통과 (1.35ms, 28MB)
테스트 25 〉	통과 (2.93ms, 27.9MB)
테스트 26 〉	통과 (1.65ms, 27.8MB)
테스트 27 〉	통과 (0.27ms, 27.7MB)
테스트 28 〉	통과 (0.24ms, 27.9MB)
    
    '''