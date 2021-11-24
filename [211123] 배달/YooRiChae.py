# 어디서 문제가 생기는걸까요....??ㅠㅠ

import heapq

def solution(N, road, K):
    graph = {}
    for i in range(1,N+1):
        graph[i] = {}
    
    for start, destination, distance in road:
        if destination in graph[start]:
            if graph[start][destination] > distance:
                graph[start][destination] = distance
                graph[destination][start] = distance
        else:
            graph[start][destination] = distance
            graph[destination][start] = distance
            
    def dijkstra(graph, start):
        queue = []
        distances = {town:float('inf') for town in graph}
        distances[start] = 0
        heapq.heappush(queue, [start, distances[start]])
        
        while queue:
            current_town, current_distance = heapq.heappop(queue)
            if distances[current_town] < current_distance:
                continue
            
            for new_town, new_distance in graph[current_town].items():
                distance = current_distance + new_distance
                if distance < distances[new_town]:
                    distances[new_town] = distance
                    heapq.heappush(queue, [new_town, distance])
        return distances
                        
    distances = dijkstra(graph, 1)
    answer = 0
    for distance in distances.values():
        if distance <= K:
            answer+=1

    return answer


'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.04ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.4MB)
테스트 12 〉	통과 (0.05ms, 10.3MB)
테스트 13 〉	통과 (0.05ms, 10.3MB)
테스트 14 〉	통과 (0.44ms, 10.4MB)
테스트 15 〉	통과 (1.02ms, 10.4MB)
테스트 16 〉	통과 (0.03ms, 10.3MB)
테스트 17 〉	통과 (0.04ms, 10.3MB)
테스트 18 〉	통과 (0.37ms, 10.3MB)
테스트 19 〉	통과 (1.15ms, 10.4MB)
테스트 20 〉	통과 (0.25ms, 10.3MB)
테스트 21 〉	통과 (0.72ms, 10.5MB)
테스트 22 〉	통과 (0.38ms, 10.3MB)
테스트 23 〉	통과 (0.79ms, 10.5MB)
테스트 24 〉	통과 (0.74ms, 10.3MB)
테스트 25 〉	통과 (1.57ms, 10.6MB)
테스트 26 〉	통과 (0.88ms, 10.5MB)
테스트 27 〉	통과 (0.97ms, 10.5MB)
테스트 28 〉	통과 (0.88ms, 10.7MB)
테스트 29 〉	통과 (1.20ms, 10.6MB)
테스트 30 〉	통과 (1.02ms, 10.6MB)
테스트 31 〉	통과 (0.06ms, 10.4MB)
테스트 32 〉	통과 (0.08ms, 10.3MB)
'''