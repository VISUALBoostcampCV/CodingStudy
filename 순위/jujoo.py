# -- 1
from collections import defaultdict
def solution(n, results):
    answer = 0
    win = defaultdict(set) # 이긴 player 저장
    lose = defaultdict(set) # 진 player 저장
    
    for winner, loser in results:
        win[winner].add(loser)
        lose[loser].add(winner)
    
    for player in range(1, n + 1):
        # player를 이긴 winner -> winner를 이긴 player도 이길 수 있음
        for winner in lose[player]: 
            win[winner] |= win[player]
        # player에게 진 loser -> loser에게 진 player에게도 짐
        for loser in win[player]:
            lose[loser] |= lose[player]

    for player in range(1, n + 1):
        if len(win[player]) + len(lose[player]) == n - 1:
            answer += 1
            
    return answer

# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.02ms, 10.3MB)
# 테스트 3 〉	통과 (0.03ms, 10.2MB)
# 테스트 4 〉	통과 (0.02ms, 10.2MB)
# 테스트 5 〉	통과 (0.26ms, 10.3MB)
# 테스트 6 〉	통과 (0.49ms, 10.3MB)
# 테스트 7 〉	통과 (1.57ms, 10.5MB)
# 테스트 8 〉	통과 (3.45ms, 11MB)
# 테스트 9 〉	통과 (4.51ms, 11.3MB)
# 테스트 10 〉	통과 (4.36ms, 11.4MB)