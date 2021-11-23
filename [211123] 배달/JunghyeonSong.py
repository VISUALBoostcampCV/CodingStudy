from collections import defaultdict

def solution(N, road, K):    
    # 도로 정보 딕셔너리로 저장
    road_dict = defaultdict(list)
    for start, end, time in road:
        road_dict[start].append((end, time))
        road_dict[end].append((start, time))
    
    # 배달 가능한 마을 자기 마을은 무조건 가능
    can_delivery = set([1])
    
    # 방문 여부 기록할 리스트
    visited = [float('inf') for n in range(N)]
    visited[0] = 0
    
    # 배달 가능한지 탐색하는 함수
    def delivery(pre_town, pre_time):
        for next_town, next_time in road_dict[pre_town]:
            # 시간 초과
            time = pre_time + next_time
            if time > K:
                continue
            
            # 더 짧은 시간 걸려서 왔으면 탐색
            if visited[next_town-1] > time:
                can_delivery.add(next_town)
                visited[next_town-1] = time
                delivery(next_town, time)
    
    # 1번 마을을 시작으로 탐색
    delivery(1, 0)
        
    return len(can_delivery)


'''
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.03ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.05ms, 10.2MB)
테스트 13 〉	통과 (0.04ms, 10.3MB)
테스트 14 〉	통과 (0.34ms, 10.5MB)
테스트 15 〉	통과 (1.16ms, 10.6MB)
테스트 16 〉	통과 (0.03ms, 10.2MB)
테스트 17 〉	통과 (0.03ms, 10.3MB)
테스트 18 〉	통과 (0.13ms, 10.4MB)
테스트 19 〉	통과 (0.44ms, 10.5MB)
테스트 20 〉	통과 (0.15ms, 10.3MB)
테스트 21 〉	통과 (0.65ms, 10.7MB)
테스트 22 〉	통과 (0.23ms, 10.2MB)
테스트 23 〉	통과 (1.14ms, 10.4MB)
테스트 24 〉	통과 (0.72ms, 10.5MB)
테스트 25 〉	통과 (1.72ms, 10.5MB)
테스트 26 〉	통과 (1.75ms, 10.5MB)
테스트 27 〉	통과 (1.24ms, 10.5MB)
테스트 28 〉	통과 (2.05ms, 10.7MB)
테스트 29 〉	통과 (2.46ms, 10.8MB)
테스트 30 〉	통과 (1.08ms, 10.5MB)
테스트 31 〉	통과 (0.06ms, 10.3MB)
테스트 32 〉	통과 (0.33ms, 10.2MB)
'''