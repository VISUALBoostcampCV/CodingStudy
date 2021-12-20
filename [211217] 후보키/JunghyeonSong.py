from itertools import combinations

def solution(relation):
    # colmun 길이 1인경우
    if len(relation[0]) == 1:
        return 1
    
    answer = 0
    
    row_num = len(relation)
    col_num = len(relation[0])
            
    # 유일성 검사를 위해 column 기준으로 리스트 생성
    columns = [[] for i in range(col_num)]
    for row in relation:
        for i, col in enumerate(row):
            columns[i].append(col)
    
    # column 하나여도 후보 키인 경우 체크
    candidate = []
    for c in range(col_num):
        if row_num == len(set(columns[c])):
            candidate.append(tuple([c]))
            answer += 1
    
    # 그 외 조합에서 유일성 & 최소성 만족하는 경우 체크    
    candidate_combi =  [c for num in range(2, col_num+1) for c in combinations(range(col_num), num)]
    for combi in candidate_combi:
        if row_num == len(set(zip(*[columns[c] for c in combi]))):
            for candi in candidate:
                if set(candi) & set(combi) == set(candi):
                    break
            else:
                answer += 1
                candidate.append(combi)
                
    return answer


'''
테스트 1 〉	통과 (0.04ms, 10.4MB)
테스트 2 〉	통과 (0.05ms, 10.3MB)
테스트 3 〉	통과 (0.04ms, 10.3MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (0.04ms, 10.3MB)
테스트 6 〉	통과 (0.00ms, 10.4MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.05ms, 10.3MB)
테스트 10 〉	통과 (0.08ms, 10.3MB)
테스트 11 〉	통과 (0.10ms, 10.2MB)
테스트 12 〉	통과 (0.48ms, 10.3MB)
테스트 13 〉	통과 (0.17ms, 10.4MB)
테스트 14 〉	통과 (0.03ms, 10.3MB)
테스트 15 〉	통과 (0.03ms, 10.3MB)
테스트 16 〉	통과 (0.04ms, 10.3MB)
테스트 17 〉	통과 (0.03ms, 10.3MB)
테스트 18 〉	통과 (1.09ms, 10.3MB)
테스트 19 〉	통과 (0.65ms, 10.3MB)
테스트 20 〉	통과 (1.11ms, 10.2MB)
테스트 21 〉	통과 (0.59ms, 10.3MB)
테스트 22 〉	통과 (0.47ms, 10.4MB)
테스트 23 〉	통과 (0.05ms, 10.3MB)
테스트 24 〉	통과 (1.22ms, 10.3MB)
테스트 25 〉	통과 (0.88ms, 10.3MB)
테스트 26 〉	통과 (0.58ms, 10.3MB)
테스트 27 〉	통과 (0.15ms, 10.2MB)
테스트 28 〉	통과 (0.15ms, 10.3MB)
'''