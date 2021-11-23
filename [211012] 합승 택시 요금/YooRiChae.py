def dijkstra(start, graph, distance):
    q = []
    q.append((0,start))
    distance[start] = 0
    
    while len(q)!=0:
        dist, now = q.pop()
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                q.append((cost, i[0]))

def solution(n, s, a, b, fares):
    INF = 100001 * (n-1)
    answer = []
    
    graph = [[]for i in range(n + 1)]
    for start, end, fare in fares:
        graph[start].append((end, fare))
        graph[end].append((start, fare))
        
    s_distance = [INF] * (n + 1)
    dijkstra(s, graph, s_distance)
    
    for i in range(1, n+1):
        a_distance = [INF] * (n + 1)
        b_distance = [INF] * (n + 1)
        dijkstra(i, graph, a_distance)
        dijkstra(i, graph, b_distance)
        answer.append(s_distance[i]+a_distance[a]+b_distance[b])
    return min(answer)

'''
정확성 테스트
테스트 1 〉	통과 (0.07ms, 10.2MB)
테스트 2 〉	통과 (0.05ms, 10.3MB)
테스트 3 〉	통과 (0.07ms, 10.3MB)
테스트 4 〉	통과 (0.47ms, 10.4MB)
테스트 5 〉	통과 (0.21ms, 10.3MB)
테스트 6 〉	통과 (0.46ms, 10.3MB)
테스트 7 〉	통과 (0.52ms, 10.3MB)
테스트 8 〉	통과 (0.90ms, 10.3MB)
테스트 9 〉	통과 (0.89ms, 10.3MB)
테스트 10 〉통과 (1.16ms, 10.3MB)

효율성 테스트
테스트 1 〉	통과 (407.40ms, 10.2MB)
테스트 2 〉	통과 (3523.25ms, 10.7MB)
테스트 3 〉	통과 (891.61ms, 10.3MB)
테스트 4 〉	통과 (889.09ms, 10.2MB)
테스트 5 〉	통과 (1007.23ms, 10.2MB)
테스트 6 〉	통과 (1020.65ms, 10.3MB)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	통과 (1807.79ms, 15.4MB)
테스트 10 〉통과 (1574.53ms, 15.5MB)
테스트 11 〉통과 (1587.24ms, 15.5MB)
테스트 12 〉실패 (시간 초과)
테스트 13 〉실패 (시간 초과)
테스트 14 〉실패 (시간 초과)
테스트 15 〉실패 (시간 초과)
테스트 16 〉통과 (727.97ms, 10.2MB)
테스트 17 〉통과 (800.84ms, 10.3MB)
테스트 18 〉통과 (747.98ms, 10.3MB)
테스트 19 〉통과 (3748.25ms, 10.5MB)
테스트 20 〉통과 (6034.32ms, 10.7MB)
테스트 21 〉통과 (5461.49ms, 10.7MB)
테스트 22 〉실패 (시간 초과)
테스트 23 〉실패 (시간 초과)
테스트 24 〉실패 (시간 초과)
테스트 25 〉통과 (268.49ms, 10.3MB)
테스트 26 〉통과 (238.50ms, 10.3MB)
테스트 27 〉통과 (4853.87ms, 10.5MB)
테스트 28 〉통과 (4856.66ms, 10.5MB)
테스트 29 〉통과 (186.32ms, 10.2MB)
테스트 30 〉통과 (239.93ms, 10.2MB)
'''