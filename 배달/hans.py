from collections import defaultdict

def solution(N, road, K):
    answer = set([0])
    distance = [500000]*N
    distance[0] = 0
    cost_map = defaultdict(list)
    
    for i,j,cost in road:
        i,j = i-1,j-1
        cost_map[i].append((j,cost))
        cost_map[j].append((i,cost))
    
    def dp(city):
        for idx,c in cost_map[city]:
            if distance[city]+c<distance[idx]:
                distance[idx] = distance[city]+c
                dp(idx)
    dp(0)        

    return len([d for d in distance if d<=K])

    '''
    테스트 1 〉	통과 (0.02ms, 10.3MB)
    테스트 2 〉	통과 (0.02ms, 10.4MB)
    테스트 3 〉	통과 (0.02ms, 10.3MB)
    테스트 4 〉	통과 (0.03ms, 10.3MB)
    테스트 5 〉	통과 (0.04ms, 10.3MB)
    테스트 6 〉	통과 (0.01ms, 10.3MB)
    테스트 7 〉	통과 (0.02ms, 10.3MB)
    테스트 8 〉	통과 (0.04ms, 10.3MB)
    테스트 9 〉	통과 (0.01ms, 10.2MB)
    테스트 10 〉	통과 (0.03ms, 10.2MB)
    테스트 11 〉	통과 (0.02ms, 10.3MB)
    테스트 12 〉	통과 (0.04ms, 10.3MB)
    테스트 13 〉	통과 (0.04ms, 10.3MB)
    테스트 14 〉	통과 (36.35ms, 10.4MB)
    테스트 15 〉	통과 (47.03ms, 10.6MB)
    테스트 16 〉	통과 (0.03ms, 10.3MB)
    테스트 17 〉	통과 (0.03ms, 10.2MB)
    테스트 18 〉	통과 (3.61ms, 10.3MB)
    테스트 19 〉	통과 (51.99ms, 10.6MB)
    테스트 20 〉	통과 (2.37ms, 10.4MB)
    테스트 21 〉	통과 (96.21ms, 10.4MB)
    테스트 22 〉	통과 (12.23ms, 10.3MB)
    테스트 23 〉	통과 (82.88ms, 10.4MB)
    테스트 24 〉	통과 (37.33ms, 10.5MB)
    테스트 25 〉	통과 (146.00ms, 10.5MB)
    테스트 26 〉	통과 (120.32ms, 10.6MB)
    테스트 27 〉	통과 (108.30ms, 10.5MB)
    테스트 28 〉	통과 (104.69ms, 10.7MB)
    테스트 29 〉	통과 (152.75ms, 10.7MB)
    테스트 30 〉	통과 (15.42ms, 10.6MB)
    테스트 31 〉	통과 (0.05ms, 10.2MB)
    테스트 32 〉	통과 (0.51ms, 10.3MB)
    '''