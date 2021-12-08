from collections import defaultdict

def solution(info, query):
    answer = []
    info_dict = defaultdict(set)
    score_list = []
    
    # 각 지원자 정보 저장
    for index, person in enumerate(info):
        p_info = person.split()
        
        for select in p_info[:-1]:
            info_dict[select].add(index)
        
        # 점수는 검색을 위해 따로 저장
        score_list.append((int(p_info[-1]), index))
    
    # 이진탐색을 위한 정렬
    score_list.sort()
    
    # 점수 이진탐색하는 함수
    def score_index_search(start=0, end=len(info)):
        m = (start + end) // 2
        if score_list[m][0] < score:
            if score_list[m+1][0] >= score:
                return m+1
            return score_index_search(m, end)
        
        return score_index_search(start, m)
    
    
    # 쿼리 가지고 조건에 맞는 사람 검색
    for q in query:
        condition = q.split(' and ')
        condition[-1], score = condition[-1].split()
        score = int(score)
        
        people = set(range(len(info)))
        
        # 점수 외에 조건이 있는 경우
        if set(condition) != {'-'}:
            for c in condition:
                # 모든 사람이 해당하는 조건인 경우 넘어감
                if c =='-' or len(info_dict[c]) == len(info):
                    continue

                people &= info_dict[c]
        
        # 사람 수 세기
        count = 0
        if score_list[0][0] >= score:
            count = len(people)
        elif score_list[-1][0] < score:
            count = 0
        else:
            index = score_index_search()
            _people = set(map(lambda x: x[1], score_list[index:]))
            count = len(people & _people)
                
        answer.append(count)
        
    return answer


    '''
    정확성  테스트
    테스트 1 〉	통과 (0.11ms, 10.5MB)
    테스트 2 〉	통과 (0.12ms, 10.5MB)
    테스트 3 〉	통과 (0.56ms, 10.5MB)
    테스트 4 〉	통과 (4.82ms, 10.6MB)
    테스트 5 〉	통과 (13.37ms, 10.6MB)
    테스트 6 〉	통과 (27.11ms, 10.6MB)
    테스트 7 〉	통과 (15.59ms, 10.8MB)
    테스트 8 〉	통과 (65.30ms, 14.1MB)
    테스트 9 〉	통과 (74.72ms, 14MB)
    테스트 10 〉	통과 (73.99ms, 14.1MB)
    테스트 11 〉	통과 (12.93ms, 10.6MB)
    테스트 12 〉	통과 (26.92ms, 10.6MB)
    테스트 13 〉	통과 (16.10ms, 10.8MB)
    테스트 14 〉	통과 (62.78ms, 12.1MB)
    테스트 15 〉	통과 (62.65ms, 12.1MB)
    테스트 16 〉	통과 (13.76ms, 10.5MB)
    테스트 17 〉	통과 (27.51ms, 10.7MB)
    테스트 18 〉	통과 (65.08ms, 12MB)
    효율성  테스트
    테스트 1 〉	실패 (시간 초과)
    테스트 2 〉	실패 (시간 초과)
    테스트 3 〉	실패 (시간 초과)
    테스트 4 〉	실패 (시간 초과)
    '''