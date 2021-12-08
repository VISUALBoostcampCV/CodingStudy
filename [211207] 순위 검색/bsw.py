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

'''O(24*query*log_2(info))'''
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
