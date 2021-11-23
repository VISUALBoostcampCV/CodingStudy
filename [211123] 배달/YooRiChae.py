# 어디서 문제가 생기는걸까요....??ㅠㅠ

import heapq

def solution(N, road, K):
    graph = {}
    for i in range(1,N+1):
        graph[i] = {}
    
    for start, destination, distance in road:
        if start > destination:
            start, destination = destination, start
        if destination in graph[start]:
            if graph[start][destination] > distance:
                graph[start][destination] = distance
        else:
            graph[start][destination] = distance
            
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
테스트 1 〉	실패 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	실패 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	실패 (0.02ms, 10.3MB)
테스트 7 〉	실패 (0.03ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.4MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	실패 (0.02ms, 10.3MB)
테스트 11 〉	실패 (0.02ms, 10.3MB)
테스트 12 〉	실패 (0.03ms, 10.3MB)
테스트 13 〉	실패 (0.04ms, 10.3MB)
테스트 14 〉	실패 (0.45ms, 10.3MB)
테스트 15 〉	실패 (0.32ms, 10.4MB)
테스트 16 〉	실패 (0.02ms, 10.3MB)
테스트 17 〉	실패 (0.02ms, 10.3MB)
테스트 18 〉	실패 (0.18ms, 10.4MB)
테스트 19 〉	실패 (0.38ms, 10.4MB)
테스트 20 〉	실패 (0.18ms, 10.4MB)
테스트 21 〉	실패 (0.41ms, 10.5MB)
테스트 22 〉	실패 (0.16ms, 10.3MB)
테스트 23 〉	실패 (0.39ms, 10.6MB)
테스트 24 〉	실패 (0.32ms, 10.4MB)
테스트 25 〉	실패 (0.54ms, 10.5MB)
테스트 26 〉	실패 (0.52ms, 10.5MB)
테스트 27 〉	실패 (0.51ms, 10.5MB)
테스트 28 〉	실패 (0.49ms, 10.5MB)
테스트 29 〉	실패 (0.56ms, 10.5MB)
테스트 30 〉	통과 (0.43ms, 10.5MB)
테스트 31 〉	통과 (0.09ms, 10.4MB)
테스트 32 〉	통과 (0.12ms, 10.3MB)
'''