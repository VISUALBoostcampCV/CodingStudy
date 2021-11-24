from collections import defaultdict, deque
def solution(N, road, K):
    answer = defaultdict(int)
    root = defaultdict(list)
    # 시작 node에서 branch 되는 (마을, 소요시간)을 추가
    for left, right, time in road:
        if right != 1:
            root[left].append((right, time))
        if left != 1:
            root[right].append((left, time))
    
    q = deque([(1, 0)])
    while q:
        cur_node, cur_time = q.popleft()
        for nxt_node, nxt_time in root[cur_node]:
            # 1. 현재 소요시간이 이전에 지났던 소요시간보다 작다면 update & K 보다 작아야함
            # 2. 소요시간이 K보다 작고 answer에 없다면 추가
            if (nxt_node not in answer or nxt_node in answer and answer[nxt_node] > cur_time + nxt_time) and cur_time + nxt_time <= K:
                answer[nxt_node] = cur_time + nxt_time
                q.append((nxt_node, answer[nxt_node]))
    return len(answer) + 1 # 1번 마을은 무조건 배달되므로 + 1

# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.02ms, 10.3MB)
# 테스트 3 〉	통과 (0.02ms, 10.4MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.02ms, 10.3MB)
# 테스트 6 〉	통과 (0.01ms, 10.3MB)
# 테스트 7 〉	통과 (0.02ms, 10.3MB)
# 테스트 8 〉	통과 (0.02ms, 10.4MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.02ms, 10.3MB)
# 테스트 11 〉	통과 (0.02ms, 10.3MB)
# 테스트 12 〉	통과 (0.03ms, 10.2MB)
# 테스트 13 〉	통과 (0.03ms, 10.3MB)
# 테스트 14 〉	통과 (0.40ms, 10.5MB)
# 테스트 15 〉	통과 (0.73ms, 10.6MB)
# 테스트 16 〉	통과 (0.02ms, 10.3MB)
# 테스트 17 〉	통과 (0.03ms, 10.2MB)
# 테스트 18 〉	통과 (0.14ms, 10.3MB)
# 테스트 19 〉	통과 (0.49ms, 10.5MB)
# 테스트 20 〉	통과 (0.14ms, 10.3MB)
# 테스트 21 〉	통과 (0.70ms, 10.6MB)
# 테스트 22 〉	통과 (0.21ms, 10.3MB)
# 테스트 23 〉	통과 (0.94ms, 10.7MB)
# 테스트 24 〉	통과 (1.09ms, 10.5MB)
# 테스트 25 〉	통과 (1.12ms, 10.5MB)
# 테스트 26 〉	통과 (1.20ms, 10.7MB)
# 테스트 27 〉	통과 (2.38ms, 10.6MB)
# 테스트 28 〉	통과 (1.36ms, 10.8MB)
# 테스트 29 〉	통과 (1.67ms, 10.6MB)
# 테스트 30 〉	통과 (1.31ms, 10.5MB)
# 테스트 31 〉	통과 (0.05ms, 10.2MB)
# 테스트 32 〉	통과 (0.09ms, 10.3MB)