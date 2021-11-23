# 가중치 그래프 -> 다익스트라
from heapq import heappush, heappop

def solution(n, s, a, b, fares):
    answer = 1e9
    INF = 1e9
    
    graph=[[] for _ in range(n+1)]
    
    for fare in fares:
        src, dst, cost = fare
        graph[src].append((dst, cost))
        graph[dst].append((src, cost))
    print(graph)
    
    def dijk(s, d):
        dists = [INF for i in range(n+1)]
        dists[s] = 0
        pq = []
        heappush(pq, (dists[s], s))
    
        # print(dists)
        # print(pq)
        while pq:
            cur_dist, cur_dst = heappop(pq)
            
            if dists[cur_dst] < cur_dist:
                continue
        
            for new_dst, new_dist in graph[cur_dst]:

                if cur_dist + new_dist < dists[new_dst]:
                    dists[new_dst] = cur_dist + new_dist
                    heappush(pq, (dists[new_dst], new_dst))
        
        
        # print(dists)
        return(dists[d])
    
    for i in range(1, n+1):
        answer = min(dijk(s, i) + dijk(i,a) + dijk(i,b), answer)
    
    return answer
