# for문에서 list 탐색하느라 오래걸리는 버전
def solution(s):
    tuples = [list(map(int, _s.split(','))) for _s in s[2:-2].split('},{')]
    tuples.sort(key=len)
    
    answer = []
    for tp in tuples:
        for t in tp:
            if t not in answer:
                answer.append(int(t))
    
    return answer


'''
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.06ms, 10.3MB)
테스트 5 〉	통과 (0.38ms, 10.3MB)
테스트 6 〉	통과 (1.03ms, 10.4MB)
테스트 7 〉	통과 (22.35ms, 11.2MB)
테스트 8 〉	통과 (105.23ms, 12.9MB)
테스트 9 〉	통과 (35.81ms, 11.7MB)
테스트 10 〉	통과 (120.43ms, 12.8MB)
테스트 11 〉	통과 (172.95ms, 14.4MB)
테스트 12 〉	통과 (285.97ms, 16.5MB)
테스트 13 〉	통과 (281.05ms, 16.5MB)
테스트 14 〉	통과 (297.30ms, 16.7MB)
테스트 15 〉	통과 (0.03ms, 10.3MB)
'''


# for문에서 set 탐색해서 빨리 탐색하는 버전
def solution(s):
    tuples = [list(map(int, _s.split(','))) for _s in s[2:-2].split('},{')]
    tuples.sort(key=len)
    
    answer = []
    search_set = set({})
    for tp in tuples:
        for t in tp:
            if t not in search_set:
                answer.append(int(t))
                search_set.add(t)
    
    return answer


'''
테스트 1 〉	통과 (0.03ms, 10.5MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (0.04ms, 10.4MB)
테스트 5 〉	통과 (0.14ms, 10.4MB)
테스트 6 〉	통과 (0.48ms, 10.4MB)
테스트 7 〉	통과 (3.99ms, 11.2MB)
테스트 8 〉	통과 (11.78ms, 12.8MB)
테스트 9 〉	통과 (5.53ms, 11.6MB)
테스트 10 〉	통과 (12.46ms, 12.9MB)
테스트 11 〉	통과 (17.46ms, 14.4MB)
테스트 12 〉	통과 (22.24ms, 16.5MB)
테스트 13 〉	통과 (23.28ms, 16.5MB)
테스트 14 〉	통과 (24.13ms, 16.7MB)
테스트 15 〉	통과 (0.02ms, 10.3MB)
'''