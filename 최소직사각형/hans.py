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