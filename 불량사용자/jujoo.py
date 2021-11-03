import re
from itertools import permutations as pm
def solution(user_id:list, banned_id:list)->int:
    banned_id = [x.replace("*", ".") for x in banned_id] # for re

    # check function
    def check(id_:set, banned_id:list)->bool:
        for i in range(len(id_)):
            if not re.findall(banned_id[i], id_[i]) or len(id_[i]) != len(banned_id[i]):
                return False
        return True

    stack = []
    # 3개 순열
    for id_ in pm(user_id, len(banned_id)):
        if check(id_, banned_id):
            id_ = set(id_)
            if id_ not in stack:
                stack.append(id_)
    return len(stack)

# 테스트 1 〉	통과 (0.05ms, 10.2MB)
# 테스트 2 〉	통과 (1.18ms, 10.3MB)
# 테스트 3 〉	통과 (0.44ms, 10.3MB)
# 테스트 4 〉	통과 (0.32ms, 10.2MB)
# 테스트 5 〉	통과 (318.48ms, 10.3MB)
# 테스트 6 〉	통과 (37.96ms, 10.2MB)
# 테스트 7 〉	통과 (4.85ms, 10.2MB)
# 테스트 8 〉	통과 (2.31ms, 10.2MB)
# 테스트 9 〉	통과 (2.52ms, 10.2MB)
# 테스트 10 〉	통과 (52.92ms, 10.2MB)
# 테스트 11 〉	통과 (3.17ms, 10.3MB)