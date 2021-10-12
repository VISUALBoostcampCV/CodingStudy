<--실패-->
from collections import deque, defaultdict
def find_path(s, target, path):
    q = deque([[s]])  # List[List[path]]
    cost = deque([0]) # List[cost]
    result = (s, 10**6)
    while q:
        cur_path= q.popleft()
        cur_cost = cost.popleft()
        if cur_path[-1] == target:
            if result > cur_cost:
                result = (cur_path, cur_cost)
            continue
            
        for nxt, nxt_cost in path[s]:
            nxt_path = cur_path + [nxt]
            if nxt_path not in q and nxt not in cur_path:
                q.append([nxt_path])
                cost.append(nxt_cost + cur_cost)
    return result

def solution(n, s, a, b, fares):
    answer = 0
    path = defaultdict(list)
    # fares 배열에 두 지점 간 예상 택시요금은 1개만 주어집니다.
    for start, end, cost in fares:
        path[start].append((end, cost))
        path[end].append((start, cost))
    
    print(find_path(s, a, path))
    
    return answer