from collections import Counter
from itertools import combinations
from functools import reduce

def solution(clothes):
    counts = Counter([x[1] for x in clothes])
    c_kind = counts.values()
    
    # 옷이 한종류만 있는경우
    if len(counts) < 2:
        return sum(c_kind)
    
    # 옷이 1개씩만 있는경우
    if set(c_kind) == set([1]):
        return 2 ** len(c_kind) - 1
    
    # 그 외의 경우
    answer = sum(c_kind) + reduce(lambda x, y: x * y, c_kind)
        
    for pick in range(2, len(counts)):
        for combi in combinations(c_kind, pick):
            answer += reduce(lambda x, y: x * y, combi)
                
        
    return answer


'''
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.08ms, 10.3MB)
테스트 4 〉	통과 (180.50ms, 10.2MB)
테스트 5 〉	통과 (0.08ms, 10.2MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (182.45ms, 10.3MB)
테스트 8 〉	통과 (1.28ms, 10.2MB)
테스트 9 〉	통과 (0.03ms, 10.2MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
테스트 11 〉	통과 (0.04ms, 10.3MB)
테스트 12 〉	통과 (4.77ms, 10.3MB)
테스트 13 〉	통과 (19.78ms, 10.3MB)
테스트 14 〉	통과 (0.03ms, 10.2MB)
테스트 15 〉	통과 (0.02ms, 10.3MB)
테스트 16 〉	통과 (0.02ms, 10.2MB)
테스트 17 〉	통과 (0.03ms, 10.2MB)
테스트 18 〉	통과 (0.14ms, 10.3MB)
테스트 19 〉	통과 (1.01ms, 10.3MB)
테스트 20 〉	통과 (0.02ms, 10.3MB)
테스트 21 〉	통과 (0.02ms, 10.2MB)
테스트 22 〉	통과 (0.02ms, 10.4MB)
테스트 23 〉	통과 (0.03ms, 10.2MB)
테스트 24 〉	통과 (0.03ms, 10.3MB)
테스트 25 〉	통과 (0.71ms, 10.4MB)
테스트 26 〉	통과 (385.14ms, 10.3MB)
테스트 27 〉	통과 (0.03ms, 10.3MB)
테스트 28 〉	통과 (0.53ms, 10.3MB)
'''



'''
옛날 풀이
'''
from collections import Counter
from functools import reduce

def solution(clothes):
    counts = Counter([x[1] for x in clothes])   # 옷 종류 세기
    answer = reduce(lambda x, y: x * (y + 1), counts.values(), 1) - 1  # 조합 구하기
    # 특정 종류의 옷을 안입는 케이스도 추가해서 y+1, 모든 종류의 옷을 안입는 케이스가 있을 수 있으니 -1
        
    return answer


'''
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.03ms, 10.2MB)
테스트 14 〉	통과 (0.02ms, 10.3MB)
테스트 15 〉	통과 (0.03ms, 10.2MB)
테스트 16 〉	통과 (0.02ms, 10.2MB)
테스트 17 〉	통과 (0.02ms, 10.2MB)
테스트 18 〉	통과 (0.02ms, 10.2MB)
테스트 19 〉	통과 (0.02ms, 10.1MB)
테스트 20 〉	통과 (0.02ms, 10.3MB)
테스트 21 〉	통과 (0.02ms, 10.2MB)
테스트 22 〉	통과 (0.02ms, 10.2MB)
테스트 23 〉	통과 (0.03ms, 10.2MB)
테스트 24 〉	통과 (0.02ms, 10.2MB)
테스트 25 〉	통과 (0.02ms, 10.2MB)
테스트 26 〉	통과 (0.03ms, 10.2MB)
테스트 27 〉	통과 (0.02ms, 10.2MB)
테스트 28 〉	통과 (0.03ms, 10.2MB)
'''