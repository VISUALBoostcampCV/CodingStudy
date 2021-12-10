from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:          # 예외 처리
        return len(cities) * 5
    
    answer = 0
    
    cache = deque()
    
    for city in cities:
        city = city.lower()
        if city in cache:           # hit
            cache.remove(city)      # cacheSize <= 30 이므로 부담없이 remove 사용
            cache.appendleft(city)  # LRU 이므로 왼쪽으로 넣는다.
            answer+=1
        elif len(cache) < cacheSize:    # miss인데 캐시가 다 안찼을 경우
            cache.appendleft(city)
            answer+=5            
        else:                           # miss이고 캐시가 다 찬 경우
            cache.pop()
            cache.appendleft(city)
            answer+=5
        
    return answer

'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.3MB)
테스트 7 〉	통과 (0.00ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉통과 (0.05ms, 10.2MB)
테스트 11 〉통과 (69.61ms, 17.6MB)
테스트 12 〉통과 (0.03ms, 10.3MB)
테스트 13 〉통과 (0.05ms, 10.4MB)
테스트 14 〉통과 (0.09ms, 10.2MB)
테스트 15 〉통과 (0.13ms, 10.3MB)
테스트 16 〉통과 (0.34ms, 10.3MB)
테스트 17 〉통과 (0.00ms, 10.3MB)
테스트 18 〉통과 (0.39ms, 10.4MB)
테스트 19 〉통과 (0.92ms, 10.3MB)
테스트 20 〉통과 (0.98ms, 10.3MB)
'''