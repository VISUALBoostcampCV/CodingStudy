import heapq

def solution(N, road, K):
    answer = 0
    
    graph = [[] for _ in range(N+1)]
    
    for i, j, cost in road:
        graph[i].append([j, cost])
        graph[j].append([i, cost])
        
    result = dijkstra(graph, 1, N)
    
    for r in result:
        if r <= K:
            answer += 1
    
    return answer


def dijkstra(graph, start, N):
    distances = [100000000 for _ in range(N+1)]
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination]:
            
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
    
    return distances
  
  
 '''
 정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.04ms, 10.2MB)
테스트 13 〉	통과 (0.06ms, 10.2MB)
테스트 14 〉	통과 (0.57ms, 10.3MB)
테스트 15 〉	통과 (0.82ms, 10.6MB)
테스트 16 〉	통과 (0.02ms, 10.4MB)
테스트 17 〉	통과 (0.06ms, 10.2MB)
테스트 18 〉	통과 (0.20ms, 10.3MB)
테스트 19 〉	통과 (0.76ms, 10.6MB)
테스트 20 〉	통과 (0.17ms, 10.3MB)
테스트 21 〉	통과 (0.93ms, 10.6MB)
테스트 22 〉	통과 (0.29ms, 10.3MB)
테스트 23 〉	통과 (0.93ms, 10.6MB)
테스트 24 〉	통과 (0.66ms, 10.7MB)
테스트 25 〉	통과 (1.58ms, 10.6MB)
테스트 26 〉	통과 (1.63ms, 10.8MB)
테스트 27 〉	통과 (1.71ms, 10.6MB)
테스트 28 〉	통과 (1.62ms, 10.7MB)
테스트 29 〉	통과 (1.55ms, 10.6MB)
테스트 30 〉	통과 (1.55ms, 10.7MB)
테스트 31 〉	통과 (0.09ms, 10.2MB)
테스트 32 〉	통과 (0.12ms, 10.3MB)
 '''
