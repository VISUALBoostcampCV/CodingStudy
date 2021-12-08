
#이전 코드

from itertools import combinations
from collections import defaultdict
import bisect
def make_cases(lst):
    cases = []
    for i in range(5):
        for c in combinations([0,1,2,3],i):
            case = ''
            for j in range(4):
                if j not in c:
                    case += lst[j]
                else:
                    case += '-'
            cases.append(case)
    return cases
def solution(info, query):
    d = defaultdict(list)
    answer = []
    for inf in info:
        inf_s = inf.split()
        cases = make_cases(inf_s)
        for case in cases:
            d[case].append(int(inf_s[-1]))
    for key in d.keys():
        d[key].sort()
        
    for q in query:
        new_q = q.split()
        new_q = new_q[:-1] + new_q[-1].split()
        score = int(new_q[-1])
        new_q = ''.join(new_q[0]+new_q[2]+new_q[4]+new_q[6])
        #print(new_q)
        answer.append(len(d[new_q]) - bisect.bisect_left(d[new_q], score))         
    
    
    return answer

'''
테스트 1 〉	통과 (0.60ms, 10.4MB)
테스트 2 〉	통과 (0.59ms, 10.4MB)
테스트 3 〉	통과 (0.86ms, 10.5MB)
테스트 4 〉	통과 (1.99ms, 10.5MB)
테스트 5 〉	통과 (3.78ms, 10.5MB)
테스트 6 〉	통과 (10.12ms, 10.5MB)
테스트 7 〉	통과 (4.15ms, 10.7MB)
테스트 8 〉	통과 (74.10ms, 11.4MB)
테스트 9 〉	통과 (76.97ms, 13.3MB)
테스트 10 〉	통과 (83.08ms, 13.8MB)
테스트 11 〉	통과 (3.49ms, 10.6MB)
테스트 12 〉	통과 (9.28ms, 10.7MB)
테스트 13 〉	통과 (4.38ms, 10.8MB)
테스트 14 〉	통과 (39.60ms, 12.1MB)
테스트 15 〉	통과 (41.33ms, 12.1MB)
테스트 16 〉	통과 (3.84ms, 10.5MB)
테스트 17 〉	통과 (9.26ms, 10.7MB)
테스트 18 〉	통과 (51.49ms, 12.1MB)
효율성  테스트
테스트 1 〉	통과 (1103.16ms, 63.7MB)
테스트 2 〉	통과 (1061.00ms, 63.9MB)
테스트 3 〉	통과 (1027.79ms, 63.5MB)
테스트 4 〉	통과 (1049.01ms, 63.9MB)
'''