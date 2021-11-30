from collections import defaultdict

def solution(clothes):
    answer = 1
    
    d = defaultdict(list)
    
    for cloth, kind in clothes:
        d[kind].append(cloth)
    
    # 안 입은 케이스를 포함 한 뒤 product
    for key in d.keys():
        answer *= len(d[key]) + 1
        
    # 아얘 안 입은 경우의 수 1개 빼줌
    return answer-1
