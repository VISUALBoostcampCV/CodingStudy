from collections import defaultdict

def solution(n, results):
    result_dict = defaultdict(dict)
    player_list = []
    rank_dict = {}
    
    def cal_rank(player):
        return 1 + sum(result_dict[player].values())
    
    def check(player):
        rank = cal_rank(player)        
        rank_dict[player] = rank    # 확실한 선수 저장
        player_list.append(player)    # 탐색을 위해 저장
    
    # 순위를 확실하게 알 수 있는 
    for winner, loser in results:
        result_dict[winner][loser] = 0  # 이긴 선수는 상대 선수와 0 저장
        result_dict[loser][winner] = 1  # 진 선수는 상대 선수와 1 저장
        
        # 순위를 확실히 알게되면 처리하기
        if len(result_dict[winner]) == n-1:
            check(winner)
            
        if len(result_dict[loser]) == n-1:
            check(loser)
    
    # 그래프 탐색
    while(player_list):
        player = player_list.pop()    # 탐색 기준 선수
        rank = rank_dict[player]
        
        # 경기했던 선수와 경기 결과 가지고 계산
        for other, result in result_dict[player].items():
            total_games = len(result_dict[other])
            win_games = cal_rank(other) - 1
            
            # 기준 선수에게 이긴 선수일 경우
            if result:                
                if total_games == rank:
                    rank_dict[other] = win_games + 1
                    player_list.append(other)
                
            # 기준 선수에게 진 선수일 경우
            else:                
                if total_games == n - rank:
                    rank_dict[other] = rank + total_games - win_games + 1
                    player_list.append(other)

        
    return len(rank_dict)


'''
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	실패 (0.01ms, 10.3MB)
테스트 3 〉	실패 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	실패 (0.13ms, 10.4MB)
테스트 6 〉	실패 (0.38ms, 10.3MB)
테스트 7 〉	실패 (0.58ms, 10.4MB)
테스트 8 〉	실패 (1.09ms, 10.6MB)
테스트 9 〉	실패 (1.49ms, 10.6MB)
테스트 10 〉	실패 (2.06ms, 11MB)
'''