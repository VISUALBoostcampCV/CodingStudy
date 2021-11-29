from collections import defaultdict
def solution(clothes):
    cnt = defaultdict(int)
    
    # 의상 종류별 개수
    for x, y in clothes:
        cnt[y] += 1
        
    answer = 1
    for i in list(cnt.values()):
        answer *= i + 1 # 입지 않았을때의 경우도 추가(+1)
    
    # 동일하지만 더 느림
    # from functools import reduce
    # answer = reduce(lambda x, y : x * (y + 1), cnt.values(), 1)
    
    return answer - 1 # 모두 입지않은 경우 -1