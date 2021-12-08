'''O(n^2)'''
# def solution(info, queries):
#     answer = []
    
#     sql = []
#     for inf in info:
#         row = list(inf.split())
#         row[-1] = int(row[-1])
#         sql.append(row)
        
#     for query in queries:
#         cnt = 0
#         row = [x for x in query.split()]
#         for i, v in enumerate(row):
#             if v == 'and':
#                 row.pop(i)
#             if v == row[-1]:
#                 row[-1] = int(v)
    
        
#         for s in sql:
#             lan_q, job_q, career_q, food_q, score_q = row
#             lan_s, job_s, career_s, food_s, score_s = s

#             if lan_q == '-':
#                 lan_q = lan_s
#             if job_q == '-':
#                 job_q = job_s
#             if career_q == '-':
#                 career_q = career_s
#             if food_q == '-':
#                 food_q = food_s

#             if lan_q + job_q + career_q + food_q == lan_s + job_s + career_s + food_s:
#                 if score_q <= score_s:
#                     cnt+=1
                
#         answer.append(cnt)
                
#     return answer
#
# 정확성  테스트
# 테스트 1 〉	통과 (0.13ms, 10.4MB)
# 테스트 2 〉	통과 (0.23ms, 10.4MB)
# 테스트 3 〉	통과 (1.05ms, 10.5MB)
# 테스트 4 〉	통과 (9.38ms, 10.5MB)
# 테스트 5 〉	통과 (39.55ms, 10.5MB)
# 테스트 6 〉	통과 (99.97ms, 10.5MB)
# 테스트 7 〉	통과 (41.30ms, 10.6MB)
# 테스트 8 〉	통과 (192.54ms, 12.5MB)
# 테스트 9 〉	통과 (200.89ms, 12.5MB)
# 테스트 10 〉	통과 (220.28ms, 12.5MB)
# 테스트 11 〉	통과 (44.64ms, 10.5MB)
# 테스트 12 〉	통과 (95.98ms, 10.5MB)
# 테스트 13 〉	통과 (41.88ms, 10.6MB)
# 테스트 14 〉	통과 (195.01ms, 11.3MB)
# 테스트 15 〉	통과 (235.06ms, 11.4MB)
# 테스트 16 〉	통과 (39.43ms, 10.5MB)
# 테스트 17 〉	통과 (95.32ms, 10.5MB)
# 테스트 18 〉	통과 (190.39ms, 11.4MB)
# 효율성  테스트
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)


'''O(24*N*log(M))'''
from collections import defaultdict
from itertools import product
def solution(info, queries):
    answer = []
    
    db = defaultdict(list)
    for inf in info:
        row = list(inf.split())
        row[-1] = int(row[-1])
        db[''.join(row[:-1])].append(row[-1])
    
    # 이진탐색을 위해 유저의 점수를 오름차순으로 저장
    for data in db.values():
        data.sort()
    
    # product를 활용하기 위해 선언한 리스트
    lang = ['cpp', 'java', 'python']
    job = ['backend', 'frontend']
    career = ['junior','senior']
    food = ['chicken', 'pizza']
    
    for query in queries:
        d={0 : lang, 1 : job, 2 : career, 3 : food}
        
        cnt = 0
        row = [x for x in query.split()] # row[-1] = 기준 점수
        for i, v in enumerate(row):
            if v == 'and':
                row.pop(i)
            if v == row[-1]:
                row[-1] = int(v)
        
        # query의 data가 '-'가 아닌 경우 해당 정보만 사용해야 하므로 위에서 선언한 리스트를 단일 정보로 변경
        for i, v in enumerate(row):
            if i == 4:
                continue
            if v != '-':
                d[i] = [v]
        
        # query 한 줄로 만들수 있는 모든 정보의 갯수를 db에서 탐색하여 cnt에 더해준다.
        # 효율성을 위해 이진탐색 사용
        for p in product(d[0], d[1], d[2], d[3]):
            cnt += BSearch(db[''.join(p)], row[-1])
        answer.append(cnt)    
    
    return answer

# 오름차순으로 정렬된 점수들의 리스트 scores에서
# 기준점수 lower보다 크거나 같은 수의 갯수를 return
def BSearch(scores, lower):
    start, end = 0, len(scores)-1
    while start<=end:
        mid = (start+end)//2
        if scores[mid] < lower :
            start = mid+1;
        else:
            end = mid-1
            
    return len(scores)-start;

'''
정확성  테스트
테스트 1 〉	통과 (0.15ms, 10.4MB)
테스트 2 〉	통과 (0.14ms, 10.5MB)
테스트 3 〉	통과 (0.49ms, 10.5MB)
테스트 4 〉	통과 (6.01ms, 10.5MB)
테스트 5 〉	통과 (8.86ms, 10.6MB)
테스트 6 〉	통과 (4.06ms, 10.6MB)
테스트 7 〉	통과 (8.77ms, 10.7MB)
테스트 8 〉	통과 (8.64ms, 10.6MB)
테스트 9 〉	통과 (4.59ms, 10.6MB)
테스트 10 〉	통과 (7.44ms, 10.9MB)
테스트 11 〉	통과 (5.12ms, 10.5MB)
테스트 12 〉	통과 (3.35ms, 10.6MB)
테스트 13 〉	통과 (15.84ms, 10.6MB)
테스트 14 〉	통과 (5.83ms, 10.8MB)
테스트 15 〉	통과 (3.44ms, 10.8MB)
테스트 16 〉	통과 (4.74ms, 10.5MB)
테스트 17 〉	통과 (3.29ms, 10.6MB)
테스트 18 〉	통과 (3.44ms, 10.8MB)
효율성  테스트
테스트 1 〉	통과 (1857.18ms, 35.9MB)
테스트 2 〉	통과 (967.68ms, 36.3MB)
테스트 3 〉	통과 (7918.20ms, 35.8MB)
테스트 4 〉	통과 (4175.12ms, 36.1MB)
'''
