from collections import defaultdict
from collections import Counter
from itertools import product
from math import factorial

def solution(user_id, banned_id):   
    
    answer = 0
    
    uid_dict = defaultdict(list)    # user id 길이별로 저장하는 딕셔너리
    bid_list = [] # 제재 아이디 가능 목록 저장하는 리스트
    bid_count = Counter(list(map(len, banned_id)))  # 제재 아이디 길이 세기
    
    # key: id 길이, value: user id
    for uid in user_id:
        uid_dict[len(uid)].append(uid)
    
    star = set(map(lambda x: str(set(x)), banned_id))
    
    # 제재 아이디 목록이 전부 *일경우
    if len(star) == 1:
        answer = 1
        
        for b_len in bid_count:
            n = len(uid_dict[b_len])
            r = bid_count[b_len]
            
            answer *= cal_combi(n, r)
            
        return answer
    
    
    # 비교하면서 가능한 아이디 목록 저장하기
    for bid in banned_id:
        # 제재 아이디 길이
        l = len(bid)
        
        # *로만 되어있는 제재 아이디일경우
        if set(bid) == set('*'):
            bid_list.append(uid_dict[l])
            continue
        
        # 제재 대상이면 리스트에 추가
        _bid_list = []
        for uid in uid_dict[l]:
            if is_banned_id(uid, bid):
                _bid_list.append(uid)
        
        bid_list.append(_bid_list)
    
    # 조합 구하기
    p_list = list(product(*bid_list))
    
    # 중복 없애기
    p_list = set(map(lambda x: ' '.join(set(x)), p_list))
    
    # 올바른 조합 찾기
    for p in p_list:
        if len(p.split(' ')) == len(banned_id):
            answer += 1
    
    return answer


def cal_combi(n, r):
    return factorial(n) // (factorial(n-r) * factorial(r))


def is_banned_id(uid, bid):
    for u, b in zip(uid, bid):
        if b == '*':
            continue
        if u != b:
            break
    else:
        return True
    
    return False



'''
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.12ms, 10.3MB)
테스트 3 〉	통과 (0.12ms, 10.3MB)
테스트 4 〉	통과 (0.09ms, 10.3MB)
테스트 5 〉	통과 (0.06ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.4MB)
테스트 7 〉	통과 (0.08ms, 10.3MB)
테스트 8 〉	통과 (0.08ms, 10.4MB)
테스트 9 〉	통과 (0.11ms, 10.5MB)
테스트 10 〉	통과 (0.06ms, 10.4MB)
테스트 11 〉	통과 (0.10ms, 10.3MB)
'''