import heapq as hq

def solution(sizes):
    h = []
    d = {'v':0, 'i':0}
    for size in sizes:         #전체 길이들 중 가장 큰 값과 그 인덱스(가로, 세로) 추출
        for i,s in enumerate(size):
            if d['v'] < s:
                d['v'],d['i'] = s,i
                
    for size in sizes:         #max heap으로 만들기
        hq.heappush(h, (-size[1-d['i']], -size[d['i']]))
    while(1):
        p = hq.heappop(h)
        if p[0]>=p[1]:        #돌려서 손해면 그만돌리기
            break
        hq.heappush(h, (p[1],p[0]))
        
    return -p[0]*d['v']
    
    '''
    테스트 1 〉	통과 (0.01ms, 10.3MB)
    테스트 2 〉	통과 (0.01ms, 10.1MB)
    테스트 3 〉	통과 (0.01ms, 10.3MB)
    테스트 4 〉	통과 (0.01ms, 10.3MB)
    테스트 5 〉	통과 (0.01ms, 10.3MB)
    테스트 6 〉	통과 (0.04ms, 10.4MB)
    테스트 7 〉	통과 (0.02ms, 10.3MB)
    테스트 8 〉	통과 (0.02ms, 10.3MB)
    테스트 9 〉	통과 (0.03ms, 10.3MB)
    테스트 10 〉	통과 (0.06ms, 10.2MB)
    테스트 11 〉	통과 (0.11ms, 10.3MB)
    테스트 12 〉	통과 (0.30ms, 10.3MB)
    테스트 13 〉	통과 (0.90ms, 10.4MB)
    테스트 14 〉	통과 (1.55ms, 10.4MB)
    테스트 15 〉	통과 (3.63ms, 10.8MB)
    테스트 16 〉	통과 (5.54ms, 11.5MB)
    테스트 17 〉	통과 (7.07ms, 12MB)
    테스트 18 〉	통과 (8.39ms, 12.2MB)
    테스트 19 〉	통과 (4.92ms, 12.4MB)
    테스트 20 〉	통과 (7.23ms, 12.7MB)
    
    
    '''